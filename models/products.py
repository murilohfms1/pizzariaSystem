from core.database import Base
from core.database import db

from sqlalchemy import Column, String, Integer, Numeric
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    price = Column(Numeric(10, 2), nullable=False)

    items = relationship("OrderItem", back_populates="product")