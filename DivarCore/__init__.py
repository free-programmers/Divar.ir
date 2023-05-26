from flask import Flask
from DivarConfig import Development



def create_app():
    app = Flask(__name__)
    app.config.from_object(Development)

    # register blueprints
    from DivarAuth import auth
    app.register_blueprint(auth, url_prefix="/auth")


    return app


app = create_app()

# read all views from starter app
import DivarStarter.views


