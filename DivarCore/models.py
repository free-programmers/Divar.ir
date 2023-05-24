from sqlalchemy import Column, Integer, String, BIGINT, DateTime, ForeignKey
from DivarCore.extenstion import db
from DivarCore.utils import TimeStamp

def unixtime():
    t = TimeStamp()
    return t.now_unixtime()

class BaseModel(db.Model):
    Updated_at = Column(BIGINT(), default=unixtime, nullable=False, unique=False, onupdate=unixtime)
    Created_at = Column(DateTime(), default=unixtime, nullable=False, unique=False)


class State(db.Model):
    """
        states table in db
    """
    __tablename__ = "divar_state"
    id = Column(Integer(), primary_key=True)
    stateName = Column(String(128), nullable=False, unique=False)

    cities = db.relationship("City", backref="State", lazy=True)


class City(db.Model):
    """
        cities table in db
    """
    __tablename__ = "divar_city"
    id = Column(Integer(), primary_key=True)
    cityName = Column(String(128), nullable=False, unique=False)
    stateID = Column(Integer(), ForeignKey("divar_state.id"), nullable=False)