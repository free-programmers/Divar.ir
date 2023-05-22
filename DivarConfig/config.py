import os
from pathlib import Path
import datetime


# sms api key
API_KEY = os.getenv("API_KEY")


NAME_DB = "app"
USERNAME_DB = "root"
PASSWORD_DB = ""
HOST_DB = "localhost"
PORT_DB = 3307


BASEDIR = Path(__file__).parent.parent
APP_RUNNER_CONFIG ={
    "port":8080,
    "debug":True,
    "host":"0.0.0.0"
}


class BaseConfig:
    """ base class for flask app config """
    SECRET_KEY = "57b29308-87ab-4004-8fa3-0d8f520f002c6b9e5c06322c61942b51ca1a58295906582d00afd9bfd33e97ed53061cfa0b3455a31730bfb20463a93e7a380e0f0bf770ff79ae7592ad5079ec861529bf653c"
    WTF_CSRF_SECRET_KEY = "7cdfcff48ef70cc266885924ca39d-5bf1-4ac7-b813-1ccbf1d964386cf9df29f7b812184c1ac70dba25e150c829ed421a9850ac0714ef5e0985949782cce8e2d63c9ff1e81cb9d855b4b842c0cca3155fe"

    # sqlalchemy config
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME_DB}:{PASSWORD_DB}@{HOST_DB}:{PORT_DB}/{NAME_DB}"


    # Session config
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    SESSION_COOKIE_NAME = 'DivarSessionApp'
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=16)

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
    DEBUG = False
    FLASK_DEBUG = False


class Production(BaseConfig):
    DEBUG = False
    FLASK_DEBUG = False