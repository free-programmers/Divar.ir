from sqlalchemy import Column, String, Boolean
from DivarCore.models import BaseModel

class User(BaseModel):
    """Base model for users"""
    __tablename__ = BaseModel.SetTableName("users")
    PhoneNumber = Column(String(11), unique=True, nullable=False)
    NationalCode = Column(String(11), unique=True, nullable=True)

    AccountVerified = Column(Boolean, default=False, nullable=False)
    IdentityVerified = Column(Boolean, default=False, nullable=False)

    def __str__(self):
        return f"< User {self.id} {self.PublicKey}>"

    def __repr__(self):
        return self.__str__()

    def GetPublicKey(self):
        return self.PublicKey

