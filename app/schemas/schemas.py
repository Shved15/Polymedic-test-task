from typing import Optional

from pydantic import BaseModel


class Faculty(BaseModel):
    faculty_id: int
    name: str


class Department(BaseModel):
    department_id: int
    name: str
    faculty_id: int


class CourseCreate(BaseModel):
    name: str
    department_id: int


class Course(BaseModel):
    course_id: int
    name: str
    department_id: int


class StudentGroup(BaseModel):
    group_id: int
    name: str
    course_id: int


class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    group_id: int


class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    group_id: Optional[int] = None


class Student(BaseModel):
    student_id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str
    group_id: int

    class Config:
        orm_mode = True


class Teacher(BaseModel):
    teacher_id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str
    department_id: int


class GradeCreate(BaseModel):
    student_id: int
    course_id: int
    grade: int


class GradeUpdate(BaseModel):
    grade: Optional[int] = None


class Grade(BaseModel):
    grade_id: int
    student_id: int
    course_id: int
    grade: int

    class Config:
        orm_mode = True


class BuildingBase(BaseModel):
    name: str
    address: str


class BuildingCreate(BuildingBase):
    pass


class Building(BuildingBase):
    building_id: int

    class Config:
        orm_mode = True


class ClassroomBase(BaseModel):
    classroom_number: str
    building_id: Optional[int] = None


class ClassroomCreate(ClassroomBase):
    pass


class Classroom(ClassroomBase):
    classroom_id: int

    class Config:
        orm_mode = True


class ScheduleBase(BaseModel):
    course_id: int
    teacher_id: int
    building_id: int
    classroom_id: int
    day_of_week: str
    start_time: str
    end_time: str


class ScheduleCreate(ScheduleBase):
    pass


class Schedule(ScheduleBase):
    schedule_id: int

    class Config:
        orm_mode = True


class SemesterBase(BaseModel):
    name: str
    start_date: str
    end_date: str


class SemesterCreate(SemesterBase):
    pass


class Semester(SemesterBase):
    semester_id: int

    class Config:
        orm_mode = True


class ExamBase(BaseModel):
    course_id: int
    teacher_id: int
    semester_id: int
    exam_datetime: str
    duration: int


class ExamCreate(ExamBase):
    pass


class Exam(ExamBase):
    exam_id: int

    class Config:
        orm_mode = True


class HomeworkBase(BaseModel):
    course_id: int
    title: str
    description: str
    created_at: Optional[str] = None
    deadline: Optional[str] = None


class HomeworkCreate(HomeworkBase):
    pass


class Homework(HomeworkBase):
    homework_id: int

    class Config:
        orm_mode = True


class CourseProgramBase(BaseModel):
    course_id: int
    module_number: int
    module_title: str
    module_description: Optional[str] = None


class CourseProgramCreate(CourseProgramBase):
    pass


class CourseProgram(CourseProgramBase):
    program_id: int

    class Config:
        orm_mode = True


class CurriculumBase(BaseModel):
    department_id: int
    program_id: int
    semester_number: int


class CurriculumCreate(CurriculumBase):
    pass


class Curriculum(CurriculumBase):
    curriculum_id: int

    class Config:
        orm_mode = True



