from core.database import Base
from core.database import db

from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    
    pwd_hash = Column(String, nullable=False)
    admin = Column(Boolean, default=False)
    active = Column(Boolean)

    orders = relationship("Order", back_populates="user")