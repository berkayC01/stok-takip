from fastapi import APIRouter
from ..models.item import Item

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/")
async def list_items() -> list[Item]:
    return [Item(id=1, name="Example", quantity=10)]
