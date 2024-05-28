from sqlalchemy import Column, Integer, String, Float
from database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    summary = Column(String(255))
    price = Column(Float)
    quantity = Column(Integer)
    author = Column(String(255))
