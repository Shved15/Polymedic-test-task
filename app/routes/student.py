from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import Student as StudentModel
from app.schemas.schemas import (
    StudentCreate,
    StudentUpdate,
    Student,
)

from app.database.database import get_async_db

router = APIRouter()


@router.post("/students", response_model=Student)
async def create_student(student: StudentCreate, db: AsyncSession = Depends(get_async_db)):
    """Create a new student."""

    # Create a new instance of StudentModel with data from the request.
    db_student = StudentModel(
        first_name=student.first_name,
        last_name=student.last_name,
        email=student.email,
        phone_number=student.phone_number,
        group_id=student.group_id,
    )
    # Add the new student to the session
    db.add(db_student)
    await db.commit()
    await db.refresh(db_student)
    return db_student


@router.get("/students/{student_id}", response_model=Student)
async def get_student(student_id: int, db: AsyncSession = Depends(get_async_db)):
    """Get a student by ID."""

    # Query the database for a student with the given ID
    db_student = await db.get(StudentModel, student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    # Return the student as a response
    return Student.from_orm(db_student)


@router.put("/students/{student_id}", response_model=Student)
async def update_student(student_id: int, student_update: StudentUpdate, db: AsyncSession = Depends(get_async_db)):
    """Update a student by ID."""

    # Query the database for a student with the given ID
    db_student = await db.get(StudentModel, student_id)
    # If student is not found, raise an HTTP exception
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    # Update the student fields with the values from the request
    for field, value in student_update.dict().items():
        setattr(db_student, field, value)

    # Commit the changes to the database
    await db.commit()
    await db.refresh(db_student)
    return db_student


@router.delete("/students/{student_id}")
async def delete_student(student_id: int, db: AsyncSession = Depends(get_async_db)):
    """Delete a student by ID."""

    db_student = await db.get(StudentModel, student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    # Delete the student from the session
    await db.delete(db_student)
    await db.commit()
    return {"message": "Student deleted"}

