# All App Extensions are here

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session
from flask_jwt_extended import JWTManager
from redis import Redis
from sms_ir import SmsIr
from DivarConfig.config import SMS_API, SMS_LINE_NUMBER
from flask_wtf.csrf import CSRFProtect



ServerSessionManager = Session()
migrate = Migrate()
db = SQLAlchemy()
ServerJWTManager = JWTManager()
ServerRedis = Redis()
ServerCSRF = CSRFProtect()
SmsIR = SmsIr(
    api_key=SMS_API,
    linenumber=SMS_LINE_NUMBER
)
