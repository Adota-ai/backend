from fastapi import FastAPI
from adota_ai.routers import auth, users 

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(auth.router)
app.include_router(users.router)