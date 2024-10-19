from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from adota_ai.routers import auth, users, adoption, animals
from adota_ai.core.config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": f"{settings.PROJECT_NAME} está funcionando!"}

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(adoption.router)
app.include_router(animals.router)
