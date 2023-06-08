from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from . import schema
from . import services
from . import db


router = APIRouter(tags=["Students"], prefix="/student")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_student_registration(
    request: schema.Student, database: Session = Depends(db.get_db)
):
    student = await services.new_student_register(request, database)
    return student


@router.get("/", response_model=list[schema.DisplayStudent])
async def get_all_students(database: Session = Depends(db.get_db)):
    return await services.all_students(database)


@router.get("/{student_id}", response_model=schema.DisplayStudent)
async def get_student_by_id(student_id: int, database: Session = Depends(db.get_db)):
    return await services.get_student_by_id(student_id, database)


@router.delete(
    "/{student_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response
)
async def delete_student_by_id(student_id: int, database: Session = Depends(db.get_db)):
    return await services.delete_student_by_id(student_id, database)
