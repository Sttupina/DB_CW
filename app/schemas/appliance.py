from pydantic import BaseModel

class Appliance(BaseModel):
    name: str
    description: str | None
    type: str
    category: str
    price: float
    stock: int
    shop: str | None