import os
from sqlalchemy import Column, String, DateTime,create_engine
from sqlalchemy.ext.declarative import declarative_base

db_base = declarative_base()

class User(db_base):
    __tablename__ = "users"
    email = Column(String(30), primary_key=True)
    name = Column(String(30), nullable=False)
    pswd = Column(String(50), nullable=False)
    timestamp = Column(DateTime(timezone=True), nullable=False)

engine = create_engine(os.getenv("DATABASE_URL"))
db_base.metadata.create_all(engine)

# from datetime import datetime
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class User(db.Model):
#     __tablename__ = "users"
#     email = db.Column(db.String(30), primary_key=True)
#     name = db.Column(db.String(30), nullable=False)
#     pswd = db.Column(db.String(50), nullable=False)
#     timestamp = db.Column(db.DateTime(timezone=True), nullable=False)
