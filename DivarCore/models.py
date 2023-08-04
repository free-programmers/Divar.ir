import uuid
import datetime
from sqlalchemy import Column, Integer, String, BIGINT, DateTime
from DivarCore.extenstion import db
from DivarCore.utils import TimeStamp
from DivarConfig.config import DATABASE_TABLE_PREFIX
from DivarExceptions.database import TableNameNotProvidedError


class BaseModel(db.Model):
    """
    Base Class for all Models
    """
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    Updated_at = Column(BIGINT(), default=TimeStamp.now_unixtime, nullable=False, unique=False, onupdate=TimeStamp.now_unixtime)
    Created_at = Column(DateTime(), default=datetime.datetime.utcnow, nullable=False, unique=False)

    PublicKey = Column(String(36), nullable=False, unique=True)

    def SetPublicKey(self):
        """Set Unique Public Key For each Instance in db"""
        while True:
            token = str(uuid.uuid4())
            if self.query.filter(self.PublicKey == token).first():
                continue
            else:
                self.PublicKey = token
                break

    @staticmethod
    def SetTableName(database_name:str):
        """
        Set the name of the Table in database + table prefix
        """
        if not database_name:
            raise TableNameNotProvidedError("Database Name is not provided")
        return f"{DATABASE_TABLE_PREFIX}{database_name}"


