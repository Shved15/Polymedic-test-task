from sqlalchemy import Column, Integer, String, ForeignKey, Date, TIMESTAMP, Time, MetaData
from sqlalchemy.orm import relationship

from app.database.database import Base

metadata = MetaData()


class Faculty(Base):
    """A class representing a faculty in the university."""
    __tablename__ = "faculty"
    metadata = metadata

    faculty_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)


class Department(Base):
    """A class representing a department in the university."""
    __tablename__ = "department"
    metadata = metadata

    department_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    faculty_id = Column(Integer, ForeignKey("faculty.faculty_id"))

    faculty = relationship("Faculty", backref="departments")


class Course(Base):
    """A class representing a course in the university."""
    __tablename__ = "course"
    metadata = metadata

    course_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    department_id = Column(Integer, ForeignKey("department.department_id"))

    department = relationship("Department", backref="courses")


class StudentGroup(Base):
    """A class representing a student group in the university."""
    __tablename__ = "studentgroup"
    metadata = metadata

    group_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(10), nullable=False)
    course_id = Column(Integer, ForeignKey("course.course_id"))

    course = relationship("Course", backref="student_groups")


class Student(Base):
    """A class representing a student in the university."""
    __tablename__ = "student"
    metadata = metadata

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False)
    phone_number = Column(String(12))
    group_id = Column(Integer, ForeignKey("studentgroup.group_id"))

    group = relationship("StudentGroup", backref="students")


class Teacher(Base):
    """A class representing a teacher in the university."""
    __tablename__ = "teacher"
    metadata = metadata

    teacher_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False)
    phone_number = Column(String(12), nullable=False)
    department_id = Column(Integer, ForeignKey("department.department_id"))

    department = relationship("Department", backref="teachers")


class Grade(Base):
    """A class representing a grade in the university."""
    __tablename__ = "grade"
    metadata = metadata

    grade_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("student.student_id"))
    course_id = Column(Integer, ForeignKey("course.course_id"))
    grade = Column(Integer)

    student = relationship("Student", backref="grades")
    course = relationship("Course", backref="grades")


class Building(Base):
    __tablename__ = "building"
    metadata = metadata

    building_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    address = Column(String(255), nullable=False)


class Classroom(Base):
    __tablename__ = "classroom"
    metadata = metadata

    classroom_id = Column(Integer, primary_key=True, autoincrement=True)
    classroom_number = Column(String(5), nullable=False)
    building_id = Column(Integer, ForeignKey("building.building_id"))

    building = relationship("Building", backref="classrooms")


class Schedule(Base):
    __tablename__ = "schedule"
    metadata = metadata

    schedule_id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey("course.course_id"))
    teacher_id = Column(Integer, ForeignKey("teacher.teacher_id"))
    building_id = Column(Integer, ForeignKey("building.building_id"))
    classroom_id = Column(Integer, ForeignKey("classroom.classroom_id"))
    day_of_week = Column(String(10), nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)

    course = relationship("Course", backref="schedules")
    teacher = relationship("Teacher", backref="schedules")
    building = relationship("Building", backref="schedules")
    classroom = relationship("Classroom", backref="schedules")


class Semester(Base):
    __tablename__ = "semester"
    metadata = metadata

    semester_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)


class Exam(Base):
    __tablename__ = "exam"
    metadata = metadata

    exam_id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey("course.course_id"))
    teacher_id = Column(Integer, ForeignKey("teacher.teacher_id"))
    semester_id = Column(Integer, ForeignKey("semester.semester_id"))
    exam_datetime = Column(TIMESTAMP)
    duration = Column(Integer, nullable=False)

    course = relationship("Course", backref="exams")
    teacher = relationship("Teacher", backref="exams")
    semester = relationship("Semester", backref="exams")


class Homework(Base):
    __tablename__ = "homework"
    metadata = metadata

    homework_id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey("course.course_id"))
    title = Column(String(255), nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(Date)
    deadline = Column(Date)

    course = relationship("Course", backref="homeworks")


class CourseProgram(Base):
    __tablename__ = "courseprogram"
    metadata = metadata

    program_id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey("course.course_id"))
    module_number = Column(Integer, nullable=False)
    module_title = Column(String(128), nullable=False)
    module_description = Column(String)

    course = relationship("Course", backref="course_programs")


class Curriculum(Base):
    __tablename__ = "curriculum"
    metadata = metadata

    curriculum_id = Column(Integer, primary_key=True, autoincrement=True)
    department_id = Column(Integer, ForeignKey("department.department_id"))
    program_id = Column(Integer, ForeignKey("courseprogram.program_id"))
    semester_number = Column(Integer)

    department = relationship("Department", backref="curricula")
    program = relationship("CourseProgram", backref="curricula")
