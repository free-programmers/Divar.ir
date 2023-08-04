import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASEDIR = Path(__file__).parent.parent
APP_DEBUG = True if os.environ.get("APP_DEBUG") == "True" else False


# sms api key
API_KEY = os.environ.get("API_KEY", "NULL")


DATABASE_NAME = os.environ.get("DATABASE_NAME", "DIVAR")
DATABASE_USER = os.environ.get("DATABASE_USER", "root")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD", "")
DATABASE_HOST = os.environ.get("DATABASE_HOST", "localhost")
DATABASE_PORT = os.environ.get("DATABASE_PORT", "3306")
DATABASE_TABLE_PREFIX = os.environ.get("DATABASE_TABLE_PREFIX", "DIVAR_")

APP_RUNNER_CONFIG ={
    "port": os.environ.get("APP_PORT", 5000),
    "debug": APP_DEBUG,
    "host": os.environ.get("APP_HOST", "localhost")
}


class BaseConfig:
    """ base class for flask app config """

    FLASK_DEBUG = 1 if APP_DEBUG else 0

    SECRET_KEY = "app and app"
    WTF_CSRF_SECRET_KEY = "app and app"

    # jtw config
    JWT_SECRET_KEY = "super secure :)"

    # sqlalchemy config
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

    # redis
    REDIS_PRODUCTION_URI = os.environ.get("REDIS_PRODUCTION_URI", "redis://localhost:6379")
    REDIS_LOCAL_URI = os.environ.get("REDIS_LOCAL_URI", "redis://localhost:6379")

    REDIS_URL = REDIS_PRODUCTION_URI

    # mail config
    MAIL_SERVER = os.environ.get("MAIL_SERVER", "")
    MAIL_PORT = os.environ.get("MAIL_PORT", 587)
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME", "")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD", "")
    MAIL_USE_TLS = True if os.environ.get("MAIL_USE_TLS") == "True" else False
    MAIL_DEBUG = os.environ.get("MAIL_DEBUG", "")

    # recaptcha v3
    RECAPTCHA_PUBLIC_KEY = os.getenv("RECAPTCHA_PUBLIC_KEY")
    RECAPTCHA_PRIVATE_KEY = os.getenv("RECAPTCHA_PRIVATE_KEY")



class Development(BaseConfig):
    DEBUG = True
    FLASK_DEBUG = True


class Production(BaseConfig):
    DEBUG = False
    FLASK_DEBUG = False



SMS_API = os.environ.get("SMS_API", "")
SMS_LINE_NUMBER = os.environ.get("SMS_LINE_NUMBER", "")