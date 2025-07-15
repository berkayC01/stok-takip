from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    id: int
    name: str
    quantity: int
    expiry_date: Optional[str] = None
