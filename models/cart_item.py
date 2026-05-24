from pydantic import BaseModel


class CartItem(BaseModel):
    id: str
    name: str
    price: str
    qty: int
