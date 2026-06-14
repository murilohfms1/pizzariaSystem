from core.database import Base, db
from models.flavours import Flavour

from sqlalchemy import Column, Integer, Enum, ForeignKey, Numeric
from sqlalchemy.orm import relationship


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    flavour = Column(Enum(Flavour), nullable=False)

    unit_price = Column(Numeric(10,2), nullable=False)
    amt = Column(Integer, default=1, nullable=False)

    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="items")  