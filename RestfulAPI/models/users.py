from core.database import Base
from core.database import db


class User(Base):
    __tablename__ = 'users'
    id = db.column(db.integer, primary_key=True)
    name = db.column(db.string(50), primary_key=True)
    age = db.column(db.integer(50), nullable=False)