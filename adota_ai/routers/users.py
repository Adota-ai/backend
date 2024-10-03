from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

router = APIRouter()

class UserRegister(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str

fake_db = []

@router.post("/register")
async def register(user: UserRegister):
    existing_user = next((u for u in fake_db if u["email"] == user.email), None)
    if existing_user:
        raise HTTPException(status_code=400, detail="Usuário já registrado com este email.")

    fake_db.append(user.dict())

    return {"message": "Usuário registrado com sucesso!", "user": user}