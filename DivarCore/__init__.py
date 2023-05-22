from flask import Flask
from DivarConfig import Development

def create_app():
    app = Flask(__name__)
    app.config.from_object(Development)

    return app


app = create_app()



