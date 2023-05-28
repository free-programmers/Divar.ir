# All App Extensions are here

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session
from flask_jwt_extended import JWTManager
# from flask_wtf.csrf import CSRFProtect


session = Session()
migrate = Migrate()
db = SQLAlchemy()
jwtMNG = JWTManager()
# csrf = CSRFProtect()
