from typing import List

from fastapi import Depends, APIRouter
from sqlalchemy.sql import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.models import Teacher as TeacherModel
from app.schemas.schemas import Teacher

from ..database.database import get_async_db

router = APIRouter()


@router.get("/teachers", response_model=List[Teacher])
async def get_teachers(db: AsyncSession = Depends(get_async_db)):
    """Get all teachers."""

    async with db.begin():
        # Query the database for all teachers
        db_teachers = await db.execute(select(TeacherModel))

        # Convert the database models to the API schema
        teachers = [
            Teacher(
                teacher_id=teacher.teacher_id,
                first_name=teacher.first_name,
                last_name=teacher.last_name,
                email=teacher.email,
                phone_number=teacher.phone_number,
                department_id=teacher.department_id
            )
            for teacher in db_teachers.scalars().all()
        ]
    return teachers

