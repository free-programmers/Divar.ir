import uuid
from sqlalchemy import Column, Integer, String, Boolean
from DivarCore.models import BaseModel

class User(BaseModel):
    __tablename__ = "divar_users"
    """Base model for users"""
    PhoneNumber = Column(String(11), unique=True, nullable=False)
    NationalCode = Column(String(11), unique=True, nullable=True)

    AccountVerified = Column(Boolean, default=False, nullable=False)
    IdentityVerified = Column(Boolean, default=False, nullable=False)
    public_key = Column(String(36), nullable=False, unique=True)

    def __repr__(self):
        return f"User>> {self.id}"

    def set_public_key(self):
        """This method set a unique public key for user"""
        while True:
            key = str(uuid.uuid4())
            db_result = self.query.filter(self.public_key == key).first()
            if db_result:
                continue
            else:
                self.public_key = key
                break