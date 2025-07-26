# models.py
from sqlalchemy import Column, Integer, String, Float
from database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    retail_price = Column(Float)
    stock = Column(Integer)

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    quantity = Column(Integer)
    customer_name = Column(String)
