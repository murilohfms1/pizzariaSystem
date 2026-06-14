from core.database import Base, db
from models.status import Status

from sqlalchemy import Column, Integer, ForeignKey, Numeric, Enum
from sqlalchemy.orm import relationship

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    status = Column(Enum(Status), nullable=False)
    total = Column(Numeric(10,2), nullable=False)

    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")    
    user = relationship("User", back_populates="orders")


# mudanca no estado da db -> refazer imigracao com: alembic revision --autogenerate -m "mudanca"