# All App Extensions are here

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session
from flask_jwt_extended import JWTManager
from redis import Redis
from sms_ir import SmsIr

session = Session()
migrate = Migrate()
db = SQLAlchemy()
jwtMNG = JWTManager()
redisServer = Redis()
SmsIR = SmsIr(
    api_key="reandom",
    linenumber="random as well"
)
# csrf = CSRFProtect()
