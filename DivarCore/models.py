import uuid
import datetime
from sqlalchemy import Column, Integer, String, BIGINT, DateTime
from DivarCore.extenstion import db
from DivarCore.utils import TimeStamp

class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    Updated_at = Column(BIGINT(), default=TimeStamp.now_unixtime, nullable=False, unique=False, onupdate=TimeStamp.now_unixtime)
    Created_at = Column(DateTime(), default=datetime.datetime.utcnow, nullable=False, unique=False)

    PublicKey = Column(String(36), nullable=False, unique=True)

    def SetPublicKey(self):
        while True:
            token = str(uuid.uuid4())
            if self.query.filter(self.PublicKey == token).first():
                continue
            else:
                self.PublicKey = token
                break



# class State(db.Model):
#     """
#         states table in db
#     """
#     __tablename__ = "divar_state"
#     id = Column(Integer(), primary_key=True)
#     stateName = Column(String(128), nullable=False, unique=False)
#
#     cities = db.relationship("City", backref="State", lazy=True)
#
#
# class City(db.Model):
#     """
#         cities table in db
#     """
#     __tablename__ = "divar_city"
#     id = Column(Integer(), primary_key=True)
#     cityName = Column(String(128), nullable=False, unique=False)
#     stateID = Column(Integer(), ForeignKey("divar_state.id"), nullable=False)
