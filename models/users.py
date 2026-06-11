from core.database import Base
from core.database import db


class User(Base):
    __tablename__ = 'users'
    id = db.column(db.integer, primary_key=True)
    name = db.column(db.string(50), nullable=False)
    tel = db.column(db.string(20), nullable=False)
    email = db.column(db.string(120), nullable=False, unique=True)
    pwd_hash = db.column(db.string(255), nullable=False)