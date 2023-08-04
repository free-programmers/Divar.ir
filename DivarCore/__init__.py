from flask import Flask
from DivarConfig import BaseConfig
from DivarCore.extenstion import db, migrate, ServerRedis, ServerJWTManager

def create_app():
    app = Flask(__name__)
    app.config.from_object(BaseConfig)

    # register blueprints
    from DivarAuth import auth
    app.register_blueprint(auth, url_prefix="/auth")

    db.init_app(app)
    migrate.init_app(app=app, db=db)
    ServerRedis.from_url(app.config["REDIS_URL"])
    ServerJWTManager.init_app(app=app)

    return app


app = create_app()

# read all views from starter app
import DivarStarter.views


