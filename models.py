from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cat(Base):
    __tablename__ = "cats"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    pic = Column(BLOB)
    votes = Column(Integer)
    