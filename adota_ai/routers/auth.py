from fastapi import APIRouter

router = APIRouter()

@router.get("/auth")
def get_auth():
    return {"message": "Auth endpoint"}
