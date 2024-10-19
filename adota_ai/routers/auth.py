from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from adota_ai.core.security import hash_password, verify_password, create_access_token
import bcrypt

router = APIRouter()

class UserRegister(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

fake_db = []

@router.post("/register")
async def register(user: UserRegister):
    hashed_password = hash_password(user.password)
    fake_db.append({
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "password": hashed_password,
    })
    return {"message": "Usuário cadastrado com sucesso"}

@router.post("/login")
async def login(user: UserLogin):
    for db_user in fake_db:
        if db_user["email"] == user.email and verify_password(user.password, db_user["password"]):
            access_token = create_access_token(data={"sub": user.email})
            return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(status_code=400, detail="Email ou senha inválidos")
