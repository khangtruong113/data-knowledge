from datetime import date
from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel, ValidationError, conint, constr, validator


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

    # custom validator that take into account only that value
    @validator("gmail")
    def validate_gmail(cls, gmail: str):
        if not gmail.endswith("@gmail.com"):
            raise ValueError("Gmail must end with @gmail.com")
        return gmail

    # custom validator that take into account other values
    # values is a dictionary of all other values except level value - they can be used in validation conditions
    @validator("level")
    def validate_level_from_age(cls, level: Level, values: dict[str, Any]):
        print(
            "values exclude level that can be used for function validate_level_from_age: \n",
            values,
        )
        if level is not None:
            if level is Level.ADVANCED and values["age"] < 14:
                raise ValueError("You must be at least 14 years old to be ADVANCED")
            return level


print("--------------well-formed student---------------")
try:
    good_student = Student(
        first_name="Elon",
        last_name="Musk",
        age=52,
        date_joined=date(2003, 1, 1),
        level=3,
        gmail="elon-tesla@gmail.com",
    )
    print("Student object: \n", good_student)
except ValidationError as e:
    print(e.json())
print("---------" * 15)


print(
    "--------------student's creation fail validaton on type hint and constraints---------------"
)
try:
    error_student = Student(
        first_name="Bug",
        last_name="x",
        age=-5,
        date_joined=date(2010, 1, 1),
        level="beginner",
        gmail="bug@gmail.com",
    )
    print("Student object: \n", error_student)
except ValidationError as e:
    print(e.json())
print("---------" * 15)


print(
    "--------------student's creation fail validaton on custom validators---------------"
)
try:
    error_student = Student(
        first_name="Issue",
        last_name="Nguyen",
        age=11,
        date_joined=date(2010, 1, 1),
        level=3,
        gmail="issue@outlook.com",
    )
    print("Student object: \n", error_student)
except ValidationError as e:
    print(e.json())
print("---------" * 15)
