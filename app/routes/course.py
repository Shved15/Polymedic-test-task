from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database.database import get_async_db
from app.models.models import (
    StudentGroup as StudentGroupModel,
    Student as StudentModel,
    Course as CourseModel,
)
from app.schemas.schemas import Course, CourseCreate, Student

router = APIRouter()


@router.post("/courses", response_model=Course)
async def create_course(course: CourseCreate, db: AsyncSession = Depends(get_async_db)):
    """Create a new course."""

    # Create a new instance of CourseModel with data from the request.
    db_course = CourseModel(name=course.name, department_id=course.department_id)

    # Add the new course to the database
    db.add(db_course)
    await db.commit()
    await db.refresh(db_course)

    # Create the course schema for the response
    course_schema = Course(
        course_id=db_course.course_id,
        name=db_course.name,
        department_id=db_course.department_id
    )
    return course_schema


@router.get("/courses/{course_id}", response_model=Course)
async def get_course(course_id: int, db: AsyncSession = Depends(get_async_db)):
    """Get course by ID."""

    db_course = await db.execute(select(CourseModel).where(CourseModel.course_id == course_id))
    course = db_course.scalar()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    course_schema = Course(
        course_id=course.course_id,
        name=course.name,
        department_id=course.department_id
    )
    return course_schema


@router.get("/courses/{course_id}/students", response_model=List[Student])
async def get_course_students(course_id: int, db: AsyncSession = Depends(get_async_db)):
    """Get all students in a course"""

    # Query the database for all students in the given course
    query = (
        select(StudentModel)
        .join(StudentModel.group)
        .join(StudentGroupModel.course)
        .where(CourseModel.course_id == course_id)
    )
    db_students = await db.execute(query)
    students = db_students.scalars().all()
    return students
