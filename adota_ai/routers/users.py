from fastapi import APIRouter, HTTPException
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
    print(f"Dados recebidos: {user}")

    if user.password.strip() == "":
        raise HTTPException(status_code=400, detail="A senha não pode estar vazia.")

    print(f"Verificando a senha: '{user.password}'")
    
    existing_user = next((u for u in fake_db if u["email"] == user.email), None)
    if existing_user:
        raise HTTPException(status_code=400, detail="Usuário já registrado com este email.")

    fake_db.append(user.dict())
    
    print(fake_db)

    return {"message": "Usuário registrado com sucesso!", "user": user}


