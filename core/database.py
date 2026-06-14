from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

db = create_engine('postgresql+psycopg2://postgres:murilo@localhost:5432/postgres')

Base = declarative_base()
# cria as tabelas no banco de dados > atraves de classes em models.py

# criacao de metadados
# Base.metadata.create_all(db)