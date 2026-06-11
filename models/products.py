from core.database import Base
from core.database import db


class Product(Base):
    __tablename__ = 'products'
    id = db.column(db.integer, primary_key=True)
    name = db.column(db.string(50), primary_key=True)
    price = db.column(db.integer(50), nullable=False)