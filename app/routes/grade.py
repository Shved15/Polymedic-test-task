from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.models import Grade as GradeModel
from app.schemas.schemas import GradeCreate, GradeUpdate, Grade

from app.database.database import get_async_db

router = APIRouter()


@router.post("/grades", response_model=Grade)
async def create_grade(grade: GradeCreate, db: AsyncSession = Depends(get_async_db)):
    """Create a new grade."""

    db_grade = GradeModel(**grade.dict())
    db.add(db_grade)
    await db.commit()
    await db.refresh(db_grade)

    return Grade.from_orm(db_grade)


@router.put("/grades/{grade_id}", response_model=Grade)
async def update_grade(grade_id: int, grade_update: GradeUpdate, db: AsyncSession = Depends(get_async_db)):
    """Update existing grade by ID"""

    # get the grade
    grade = await db.execute(select(GradeModel).where(GradeModel.grade_id == grade_id))
    db_grade = grade.scalar()
    if db_grade is None:
        raise HTTPException(status_code=404, detail="Grade not found")

    if grade_update.grade is not None:
        db_grade.grade = grade_update.grade

    await db.commit()
    await db.refresh(db_grade)

    return Grade.from_orm(db_grade)
