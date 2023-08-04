import datetime
import uuid


import DivarAuth.models as AuthModel
import ExtraUtils.constans.http_status_code as status

from flask_jwt_extended import create_access_token, create_refresh_token
from flask import request, jsonify
from DivarAuth import auth
from DivarCore.utils import json_only, ArgParser
from DivarCore.extenstion import ServerRedis, db, SmsIR
from DivarAuth.utils import generate_account_verify_token, generate_login_code
from ExtraUtils.utils import send_sms



REGISTER_ARG_PARSER = ArgParser()
REGISTER_ARG_PARSER.add_rules(Fname="phonenumber", Ferror="Phone number is required")

@auth.route("/api/register/", methods=["POST"])
@json_only
@REGISTER_ARG_PARSER.verify
def register_new_user():
    """
        this view take a phone number to register user in app
    """
    args = request.get_json()
    phone = args.get("phonenumber")

    if not phone[0] == "0" or not phone[1] == "9" or not len(phone) == 11:
        return jsonify({"error": "invalid phone number"}), status.HTTP_400_BAD_REQUEST

    # check sql and redis db
    user_db = AuthModel.User.query.filter(AuthModel.User.PhoneNumber == phone).first()
    name = phone + "_register"
    redis_db = ServerRedis.get(name=name)

    if user_db or redis_db:
        return jsonify({"error": "Account already Exists"}), status.HTTP_409_CONFLICT


    token = str(uuid.uuid4())
    name = phone + "_register"
    ServerRedis.set(name=name, value=token, ex=60*6)

    name = phone + "_code"
    code = generate_account_verify_token()
    ServerRedis.set(name=name, value=code, ex=60*5)


    # send sms to user mobile
    send_sms(to=phone, msg=f"کد شما در دیوار {12} می باشد ")

    return jsonify({"message": "User Created Successfully", "token": token, "phone":phone}), \
           status.HTTP_200_OK





VERIFY_USER_ARG_PARSER = ArgParser()
VERIFY_USER_ARG_PARSER.add_rules(Fname="token", Ferror="token is required")
VERIFY_USER_ARG_PARSER.add_rules(Fname="phone", Ferror="phone is required")
VERIFY_USER_ARG_PARSER.add_rules(Fname="code", Ferror="code is required")
@auth.route("/api/verify/", methods=["POST"])
@json_only
@VERIFY_USER_ARG_PARSER.verify
def verify_user_account():
    """
        this view take a post request for verify user account
        aka: create user account in db
    """
    args = request.get_json()
    phone, code, token = args.get("phone"), args.get("code"),args.get("token")

    # check redis db for phone
    register_db = ServerRedis.get(phone + "_register")
    if not register_db:
        return jsonify({"error":"User not found!"}), status.HTTP_400_BAD_REQUEST

    code_db = ServerRedis.get(phone + "_code")
    if not code_db:
        return jsonify({"error":"User not found!"}), status.HTTP_400_BAD_REQUEST

    if AuthModel.User.query.filter(AuthModel.User.PhoneNumber == phone).first():
        return jsonify({"error":"User Registered !!"}), status.HTTP_400_BAD_REQUEST

    code_db = str(code_db.decode('utf-8'))
    register_db = str(register_db.decode('utf-8'))

    if token != register_db:
        return jsonify({"error":"Token is invalid"}), status.HTTP_400_BAD_REQUEST

    if code != code_db:
        return jsonify({"error":"code is invalid"}), status.HTTP_400_BAD_REQUEST


    new_user = AuthModel.User()
    new_user.SetPublicKey()
    new_user.PhoneNumber = phone
    new_user.AccountVerified = True
    ServerRedis.delete(phone + "_code")
    ServerRedis.delete(phone + "_register")


    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"error":"Try again!"}), status.HTTP_400_BAD_REQUEST
    else:
        return jsonify({"message":"User verify Successfully!"}), status.HTTP_200_OK



LOGIN_ARG_PARSER = ArgParser()
LOGIN_ARG_PARSER.add_rules(Fname="phone", Ferror="PhoneNumber is required")
@auth.route("/api/login/", methods=["POST"])
@json_only
@LOGIN_ARG_PARSER.verify
def login_user():
    """
        this view take a post request for login user and if it's correct return jwt token
    """
    args = request.get_json()
    phoneNumber = args.get("phone")

    if not (user_db := AuthModel.User.query.filter(AuthModel.User.PhoneNumber == phoneNumber).first()):
        return jsonify({'error':'User does not exist'}), status.HTTP_404_NOT_FOUND

    userPublicKey = user_db.GetPublicKey()


    # check user already request for logged in before
    if ServerRedis.get(userPublicKey + "_login"):
        return jsonify({"message": "User already have a request for login"}), status.HTTP_429_TOO_MANY_REQUESTS
    else:
        code = generate_login_code()

        if not ServerRedis.set(name=code, value=userPublicKey, ex=60 * 5):
            return jsonify({"error": "re-error /login/ 145"})
        if not ServerRedis.set(name=userPublicKey + "_login", value=code, ex=60 * 5):
            return jsonify({"error": "re-error /login/ 145"})

        msg = "کاربر گرامی کد ورود شما به دیوار "
        msg += code
        msg += " می باشد \n لطفا کد را در اختیار شخص دیگری قرار ندهید.\n دیوار"

        # *: this is a just a clone Version But is real world
        # Project we should check for sms send successfully
        if not SmsIR.send_sms(message=msg, number=user_db.PhoneNumber):
            pass

        return jsonify({"message": "Code Send to user", "expire_time": "300", "user_id":userPublicKey}), status.HTTP_200_OK






VERIFY_LOGIN_ARG_PARSER = ArgParser()
VERIFY_LOGIN_ARG_PARSER.add_rules(Fname="code", Ferror="code is required")
VERIFY_LOGIN_ARG_PARSER.add_rules(Fname="user_id", Ferror="user_id is required")
@auth.route("/api/login/verify/", methods=["POST"])
@json_only
@VERIFY_LOGIN_ARG_PARSER.verify
def verify_login():
    """
        this view verify loginCode that send to user phone and let user login to its account
    """
    args = request.get_json()
    code, user_id = args.get("code"),args.get("user_id")

    if not(user_code := ServerRedis.get(user_id + "_login")):
        return jsonify({"error": "login first"}), status.HTTP_400_BAD_REQUEST

    user_code = str(user_code.decode('utf-8'))
    if user_code != code:
        return jsonify({"error": "invalid code"}), status.HTTP_400_BAD_REQUEST
    else:
        ServerRedis.delete(code)
        ServerRedis.delete(user_id + "_login")

        access_token = create_access_token(identity=user_id)
        refresh_token = create_refresh_token(identity=user_id, expires_delta=datetime.timedelta(days=30))
        return jsonify({
            "access_token": access_token,
            "refresh_token": refresh_token
        }), status.HTTP_200_OK




