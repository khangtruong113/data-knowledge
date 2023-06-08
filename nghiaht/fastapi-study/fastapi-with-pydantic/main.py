from fastapi import FastAPI
from typing import Any, Optional
from datetime import date
from pydantic import BaseModel, ValidationError, conint, constr, validator
from enum import Enum
import uvicorn 


app = FastAPI()


class Level(Enum):
    BEGINNER = 1
    INTERMEDIATE = 2
    ADVANCED = 3


class Student(BaseModel):
    first_name: str
    last_name: constr(
        strip_whitespace=True, strict=True, min_length=2, curtail_length=25
    )
    age: conint(gt=0, le=150)
    date_joined: date
    level: Optional[Level]
    gmail: str

    @validator("gmail")
    def validate_gmail(cls, gmail: str):
        if not gmail.endswith("@gmail.com"):
            raise ValueError("Gmail must end with @gmail.com")
        return gmail

    @validator("level")
    def validate_level_from_age(cls, level: Level, values: dict[str, Any]):
        if level is not None:
            if level is Level.ADVANCED and values["age"] < 14:
                raise ValueError("You must be at least 14 years old to be ADVANCED")
            return level




@app.post("/")
def create_student(student: Student):
    return student.dict()


uvicorn.run(app, port=8000, host="127.0.0.1")