# All App Extensions are here

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session

session = Session()
migrate = Migrate()
db = SQLAlchemy()

