from sqlalchemy import Column, Integer, String, BIGINT
from DivarCore.extenstion import db
import datetime



class BaseModel(db.Model):
    Updated_at = Column(BIGINT(), default=)
    Created_at

class State(db.Model):
    """
    Base class model for states
    """