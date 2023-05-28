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




registerArg = ArgParser()
registerArg.add_rules(Fname="phonenumber", Ferror="Phone number is required")

@auth.route("/api/register/", methods=["POST"])
@json_only
@registerArg.verify
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

    send_sms(to=phone, msg=f"کد شما در دیوار  می باشد{12} ")

    return jsonify({"message": "User Created Successfully", "token": token, "phone":phone}), HTTP_200_OK


