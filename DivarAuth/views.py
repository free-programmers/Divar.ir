from DivarAuth import auth
from DivarCore.utils import json_only, ArgParser



loginArg = ArgParser()
loginArg.add_rules(Fname="username", Ferror="username is required")
loginArg.add_rules(Fname="password", Ferror="password is required")
@auth.route("/login/", methods=["POST"])
@json_only
@loginArg.verify
def login():
    return "OK"
