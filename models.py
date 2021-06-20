from database import Base
from sqlalchemy import Column, Integer, String, Float

class InventoryItem(Base):
    __tablename__ = "stock"

    item_id = Column(Integer,primary_key=True)
    name = Column(String)
    price = Column(Float)
    brand = Column(String)

