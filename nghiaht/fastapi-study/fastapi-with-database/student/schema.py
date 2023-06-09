from pydantic import BaseModel, constr, conint, validator
from enum import Enum
from typing import Optional
from datetime import date
from typing import Any


# class Level(Enum):
#     BEGINNER = 1
#     INTERMEDIATE = 2
#     ADVANCED = 3


class Student(BaseModel):
    first_name: str
    last_name: constr(
        strip_whitespace=True, strict=True, min_length=2, curtail_length=25
    )
    age: conint(gt=0, le=150)
    date_joined: date
    level: Optional[int]
    gmail: str

    @validator("gmail")
    def validate_gmail(cls, gmail: str):
        if not gmail.endswith("@gmail.com"):
            raise ValueError("Gmail must end with @gmail.com")
        return gmail

    # @validator("level")
    # def validate_level_from_age(cls, level: Level, values: dict[str, Any]):
    #     if level is not None:
    #         if level is Level.ADVANCED and values["age"] < 14:
    #             raise ValueError("You must be at least 14 years old to be ADVANCED")
    #         return level
        

    @validator("level")
    def validate_level_from_age(cls, level: int, values: dict[str, Any]):
        if level is not None:
            if level == 3 and values["age"] < 14:
                raise ValueError("You must be at least 14 years old to be ADVANCED")
            return level
        
class DisplayStudent(BaseModel):
    first_name: str
    last_name: str
    age: int
    date_joined: date
    level: int
    gmail: str

    class Config:
        orm_mode = True