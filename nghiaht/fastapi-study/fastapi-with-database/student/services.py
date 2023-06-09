from . import models
from . import schema

from typing import Optional
from fastapi import HTTPException, status


async def new_student_register(request, database) -> models.Student:
    new_student = models.Student(
        first_name=request.first_name,
        last_name=request.last_name,
        age=request.age,
        date_joined=request.date_joined,
        level=request.level,
        gmail=request.gmail,
    )
    database.add(new_student)
    database.commit()
    database.refresh(new_student)
    return new_student


async def all_students(database) -> list[models.Student]:
    students = database.query(models.Student).all()

    return students


async def get_student_by_id(student_id, database) -> Optional[models.Student]:
    student_info = database.query(models.Student).get(student_id)

    if not student_info:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Data Not Found !"
        )
    return student_info


async def delete_student_by_id(student_id, database):
    database.query(models.Student).filter(models.Student.id == student_id).delete()
    database.commit()
