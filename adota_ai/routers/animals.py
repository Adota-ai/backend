from fastapi import APIRouter, HTTPException
from typing import List
from adota_ai.models.animals import AnimalCreate, AnimalResponse
from adota_ai.database import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter()

animals_db = []

@router.post("/animals", response_model=AnimalResponse)
async def create_animal(animal: AnimalCreate):
    new_animal = Animal(**animal.dict())
    animals_db.append(new_animal)
    return new_animal

@router.get("/animals", response_model=List[AnimalResponse])
async def get_animals():
    return animals_db
