from sqlalchemy import Column, String, Boolean
from DivarCore.models import BaseModel

class User(BaseModel):
    __tablename__ = "divar_users"
    """Base model for users"""
    PhoneNumber = Column(String(11), unique=True, nullable=False)
    NationalCode = Column(String(11), unique=True, nullable=True)

    AccountVerified = Column(Boolean, default=False, nullable=False)
    IdentityVerified = Column(Boolean, default=False, nullable=False)

    def __str__(self):
        return f"User>> {self.id}"

    def GetPublicKey(self):
        return self.PublicKey

