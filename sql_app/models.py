from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Numeric, DateTime, func
from sqlalchemy.orm import relationship

from .database import Base



class Product(Base):
    __tablename__ = "products"


    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    desc = Column(Text, index=True)
    SKU = Column(String, index=True)
    category_id = Column(Integer)
    inventory_id = Column(Integer)
    price = Column(Numeric, index=True)
    discount_id = Column(Integer)
    created_ad = Column(DateTime(timezone=True), server_default=func.now())
    modified_ad = Column(DateTime(timezone=True), server_default=func.now())
    deleted_ad = Column(DateTime(timezone=True), server_default=func.now())

    carts_items = relationship("Cart_Item", back_populates="product")
    carts_items = relationship("Order_Items", back_populates="product")

class Cart_Item(Base):
    __tablename__ = "carts_items"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("shopping_sessions.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(String, index=True)
    created_ad = Column(DateTime(timezone=True), server_default=func.now())
    modified_ad = Column(DateTime(timezone=True), server_default=func.now())


    product = relationship("Product", back_populates="carts_items")



class Shopping_Session(Base):
    __tablename__ = "shopping_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    total = Column(Numeric, index=True)
    created_ad = Column(DateTime(timezone=True), server_default=func.now())
    modified_ad = Column(DateTime(timezone=True), server_default=func.now())


class User(Base):
    __tablename__ = "users"


    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    passord = Column(Text, index=True) 
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    adress = Column(String, index=True)
    telephone = Column(Integer, index=True)
    created_ad = Column(DateTime(timezone=True), server_default=func.now())
    modified_ad = Column(DateTime(timezone=True), server_default=func.now())

class Order_Details(Base):
    __tablename__ = "orders_details"


    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    total = Column(Numeric, index=True)
    payment_id = Column(Integer, ForeignKey("payments_details.id"))
    created_ad = Column(DateTime(timezone=True), server_default=func.now())
    modified_ad = Column(DateTime(timezone=True), server_default=func.now())

class Order_Items(Base):
    __tablename__ = "orders_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders_details.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(String, index=True)
    created_ad = Column(DateTime(timezone=True), server_default=func.now())
    modified_ad = Column(DateTime(timezone=True), server_default=func.now())

    carts_items = relationship("Product", back_populates="orders_items")

class Payment_Details(Base):
    __tablename__ = "payments_details"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer)
    product_id = Column(Integer)
    provider = Column(String, index=True)
    status = Column(String, index=True)
    created_ad = Column(DateTime(timezone=True), server_default=func.now())
    modified_ad = Column(DateTime(timezone=True), server_default=func.now())











    


