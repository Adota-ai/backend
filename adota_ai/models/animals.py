from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Animal(Base):
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    species = Column(String)
    age = Column(Integer)
    description = Column(String)
    image = Column(String)
    status = Column(String)

class AnimalCreate(BaseModel):
    name: str
    species: str
    age: int
    description: str
    image: str
    status: str

class AnimalResponse(BaseModel):
    id: int
    name: str
    species: str
    age: int
    description: str
    image: str
    status: str

    class Config:
        orm_mode = True 
