from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)

    name = Column(String(100), nullable=False)

    price = Column(Float, nullable=False)

    quantity = Column(Integer, default=0)

    description = Column(String)