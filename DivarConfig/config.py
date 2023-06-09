import os
import datetime
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
print(os.environ)

BASEDIR = Path(__file__).parent.parent

# sms api key
API_KEY = os.environ.get("API_KEY")


NAME_DB = "divar"
USERNAME_DB = "divar" # local db
PASSWORD_DB = "123654" # test password for localhost only
HOST_DB = "localhost"
PORT_DB = 3306


APP_RUNNER_CONFIG ={
    "port": 8080,
    "debug": True,
    "host": "0.0.0.0"
}


class BaseConfig:
    """ base class for flask app config """
    SECRET_KEY = "app and app"
    WTF_CSRF_SECRET_KEY = "app and app"

    # jtw config
    JWT_SECRET_KEY = "super secure :)"

    # sqlalchemy config
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME_DB}:{PASSWORD_DB}@{HOST_DB}:{PORT_DB}/{NAME_DB}"

    # redis
    REDIS_URL = "redis://localhost:6379"

    # Session config
    # SESSION_PERMANENT = False
    # SESSION_TYPE = "filesystem"
    # SESSION_COOKIE_SECURE = True
    # SESSION_COOKIE_SECURE = True
    # SESSION_COOKIE_HTTPONLY = True
    # SESSION_COOKIE_SAMESITE = 'Lax'
    # SESSION_COOKIE_NAME = 'DivarSessionApp'
    # PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=16)

    # mail config
    MAIL_SERVER = ""
    MAIL_PORT = 587
    MAIL_USERNAME = ""
    MAIL_PASSWORD = ""
    MAIL_USE_TLS = True
    MAIL_DEBUG = False

    # recaptcha v3
    RECAPTCHA_PUBLIC_KEY = os.getenv("RECAPTCHA_PUBLIC_KEY")
    RECAPTCHA_PRIVATE_KEY = os.getenv("RECAPTCHA_PRIVATE_KEY")



class Development(BaseConfig):
    DEBUG = True
    FLASK_DEBUG = True


class Production(BaseConfig):
    DEBUG = False
    FLASK_DEBUG = False