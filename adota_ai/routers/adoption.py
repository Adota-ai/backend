from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Animal(BaseModel):
    id: int
    name: str
    species: str
    age: int
    description: str
    image: str
    status: str

animals_db: List[Animal] = []

@router.post("/animals")
async def create_animal(animal: Animal):
    global animals_db
    animals_db.append(animal)
    return {"message": "Animal cadastrado com sucesso!", "animal": animal}


@router.get("/animals", response_model=List[Animal])
async def get_animals():
    global animals_db
    return animals_db