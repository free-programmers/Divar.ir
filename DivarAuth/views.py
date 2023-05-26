from DivarAuth import auth
from flask_jwt_extended import jwt_required
from DivarCore.utils import json_only, ArgParser
from flask import request


loginArg = ArgParser()
loginArg.add_rules(Fname="username", Ferror="username required")

@auth.route("/login/", methods=["POST"])
@json_only
@loginArg.verify
def login():
    return "OK"
