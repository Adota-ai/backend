from fastapi import FastAPI
from adota_ai.routers import auth, users 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
def read_root():
    return {"Message": "Mudar aqui depois dos testes"}

app.include_router(auth.router)
app.include_router(users.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)