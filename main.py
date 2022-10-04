from typing import List, Optional
from enum import Enum
from pydantic import BaseModel, Field, EmailStr
from fastapi import FastAPI, Body, Query, Path

app = FastAPI()

class HairColor(Enum):
    white: "white"
    black: "black"
    brown: "brown"

class Person(BaseModel):
    first_name: str = Field(min_length=2, max_length=20)
    last_name: str = Field(min_length=2, max_length=20)
    age: int = Field(ge=90)
    hair_color: Optional[HairColor] = Field(default=None)
    developer: bool
    email: EmailStr = Field(default="danilo@exmaple.com")
    class Config:
        schema_extra = {
            "example": {
                "first_name": "Danilo",
                "last_name": "Vilca",
                "age": 18,
                "hair_color": "black",
                "developer": True,
                "email": "vilca@gmail.com"
            }
        }

class Location(BaseModel):
    country: str
    city: str
    dirrection: Optional[str] = None
@app.get("/")
def home():
    return {"Hello": "World", "Name": 15}


@app.post("/person/new")
def create_person(person: Person = Body()):
    return person


@app.get("/persons/detail/{person}")
def obtener_person(person: str = Path(min_length=2, max_length=20)):
    return {person: "it exists"}


@app.get("/persons/me")
def obtener_person(
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        title="Person name",
        description="This is person name",
    ),
    age: str = Query(description="This is age person", title="This is tittle"),
):
    return {name: age}


@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(title="Person ID", description="ID of the person", gt=0, example=12),
    person: Person = Body(),
    # location: Location = Body(),
):
    # result = person.dict()
    # result.update(location.dict())
    return person
