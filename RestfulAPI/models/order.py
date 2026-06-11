from core.database import Base
from core.database import db


class Order(Base):
    __tablename__ = 'orders'
    id = db.column(db.integer, primary_key=True)
    user_id = db.column(db.integer, db.ForeignKey('users.id'))
    product_id = db.column(db.integer, db.ForeignKey('products.id'))
    quantity = db.column(db.integer(50), nullable=False)