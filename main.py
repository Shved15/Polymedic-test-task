from fastapi import FastAPI
from app.routes.course import router as course_router
from app.routes.student import router as student_router
from app.routes.teacher import router as teacher_router
from app.routes.grade import router as grade_router

app = FastAPI()


app.include_router(student_router)
app.include_router(teacher_router)
app.include_router(course_router)
app.include_router(grade_router)
