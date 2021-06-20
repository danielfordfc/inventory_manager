from pydantic import BaseModel


class Item(BaseModel):
    item_id: int
    name: str
    price: float
    brand: str

class UpdateItem(BaseModel):
    item_id: int = None
    name: str = None
    price: float = None
    brand: str = None