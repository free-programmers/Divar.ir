import uuid

import DivarAuth.models as AuthModel

from flask import request, jsonify
from DivarAuth import auth
from DivarCore.utils import json_only, ArgParser
from DivarCore.extenstion import redisServer, db
from DivarAuth.utils import generate_account_verify_token
from ExtraUtils.utils import send_sms
from ExtraUtils.constans.http_status_code import (
    HTTP_400_BAD_REQUEST,
    HTTP_409_CONFLICT,
    HTTP_200_OK
)




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
        return jsonify({"error": "invalid phone number"}), HTTP_400_BAD_REQUEST

    # check sql and redis db
    user_db = AuthModel.User.query.filter(AuthModel.User.PhoneNumber == phone).first()
    name = phone + "_register"
    redis_db = redisServer.get(name=name)

    if user_db or redis_db:
        return jsonify({"error": "Account already Exists"}), HTTP_409_CONFLICT


    token = str(uuid.uuid4())
    name = phone + "_register"
    redisServer.set(name=name, value=token, ex=60*6)

    name = phone + "_code"
    code = generate_account_verify_token()
    redisServer.set(name=name, value=code, ex=60*5)


    # send sms to user mobile
    send_sms(to=phone, msg=f"کد شما در دیوار {12} می باشد ")

    return jsonify({"message": "User Created Successfully", "token": token, "phone":phone}), \
           HTTP_200_OK



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
    """
    args = request.get_json()
    phone, code, token = args.get("phone"), args.get("code"),args.get("token")

    # check redis db for phone
    register_db = redisServer.get(phone+"_register")
    if not register_db:
        return jsonify({"error":"User not found!"}), HTTP_400_BAD_REQUEST

    code_db = redisServer.get(phone+"_code")
    if not code_db:
        return jsonify({"error":"User not found!"}), HTTP_400_BAD_REQUEST

    if AuthModel.User.query.filter(AuthModel.User.PhoneNumber == phone).first():
        return jsonify({"error":"User Registered !!"}), HTTP_400_BAD_REQUEST

    code_db = str(code_db.decode('utf-8'))
    register_db = str(register_db.decode('utf-8'))

    if token != register_db:
        return jsonify({"error":"Token is invalid"}), HTTP_400_BAD_REQUEST

    if code != code_db:
        return jsonify({"error":"code is invalid"}), HTTP_400_BAD_REQUEST


    new_user = AuthModel.User()
    new_user.set_public_key()
    new_user.PhoneNumber = phone
    new_user.AccountVerified = True
    redisServer.delete(phone+"_code")
    redisServer.delete(phone+"_register")


    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"error":"Try again!"}), HTTP_400_BAD_REQUEST
    else:
        return jsonify({"message":"User verify Successfully!"}), HTTP_200_OK



LOGIN_ARG_PARSER = ArgParser()
LOGIN_ARG_PARSER.add_rules(Fname="username", Ferror="Username is required")
LOGIN_ARG_PARSER.add_rules(Fname="password", Ferror="password is required")
@auth.route("/api/login/", methods=["POST"])
@json_only
@LOGIN_ARG_PARSER.verify
def login_user():
    """
        this view take a post request for login user and if it's correct return jwt token
    """
    args = request.get_json()
    username, password = args.get("username"), args.get("password")

    AuthModel.User.query.filter(AuthModel.User.).first()
