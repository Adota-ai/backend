from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
async def login(request: LoginRequest):
    if request.email == "test@example.com" and request.password == "password123":
        return {"message": "Login realizado com sucesso"}
    raise HTTPException(status_code=400, detail="Credenciais inválidas")