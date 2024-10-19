from fastapi import APIRouter

router = APIRouter()

@router.get("/items")
async def read_items():
    return [{"item_id": 1, "name": "Item 1"}, {"item_id": 2, "name": "Item 2"}]