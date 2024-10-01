from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class UserRegister(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

@router.post("/register")
async def register(user: UserRegister):
    return {"message": "Usuário registrado com sucesso!"}