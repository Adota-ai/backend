from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from adota_ai.core.security import verify_token

router = APIRouter()

fake_db = []

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar o token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    email = verify_token(token, credentials_exception)
    user = next((u for u in fake_db if u["email"] == email), None)
    if user is None:
        raise credentials_exception
    return user

@router.get("/me")
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return {"email": current_user["email"], "first_name": current_user["first_name"]}
