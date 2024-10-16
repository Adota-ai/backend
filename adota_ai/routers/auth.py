from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from adota_ai.routers.users import fake_db

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
async def login(request: LoginRequest):
    user = next((u for u in fake_db if u["email"] == request.email), None)
    
    if user:
        print(f"Usuário encontrado: {user}")
    else:
        print("Usuário não encontrado")

    if user and user["password"] == request.password:
        return {"message": "Login realizado com sucesso"}
    
    raise HTTPException(status_code=400, detail="Login falhou. Verifique suas credenciais.")



