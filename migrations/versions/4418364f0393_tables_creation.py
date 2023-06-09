"""tables creation

Revision ID: 4418364f0393
Revises: 
Create Date: 2023-06-12 22:08:24.385039

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4418364f0393'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('building',
    sa.Column('building_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('building_id')
    )
    op.create_table('faculty',
    sa.Column('faculty_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('faculty_id')
    )
    op.create_index(op.f('ix_faculty_faculty_id'), 'faculty', ['faculty_id'], unique=False)
    op.create_table('semester',
    sa.Column('semester_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('end_date', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('semester_id')
    )
    op.create_table('classroom',
    sa.Column('classroom_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('classroom_number', sa.String(length=5), nullable=False),
    sa.Column('building_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['building_id'], ['building.building_id'], ),
    sa.PrimaryKeyConstraint('classroom_id')
    )
    op.create_table('department',
    sa.Column('department_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('faculty_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['faculty_id'], ['faculty.faculty_id'], ),
    sa.PrimaryKeyConstraint('department_id')
    )
    op.create_index(op.f('ix_department_department_id'), 'department', ['department_id'], unique=False)
    op.create_table('course',
    sa.Column('course_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['department.department_id'], ),
    sa.PrimaryKeyConstraint('course_id')
    )
    op.create_index(op.f('ix_course_course_id'), 'course', ['course_id'], unique=False)
    op.create_table('teacher',
    sa.Column('teacher_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=False),
    sa.Column('last_name', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.Column('phone_number', sa.String(length=12), nullable=False),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['department.department_id'], ),
    sa.PrimaryKeyConstraint('teacher_id')
    )
    op.create_index(op.f('ix_teacher_teacher_id'), 'teacher', ['teacher_id'], unique=False)
    op.create_table('courseprogram',
    sa.Column('program_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('module_number', sa.Integer(), nullable=False),
    sa.Column('module_title', sa.String(length=128), nullable=False),
    sa.Column('module_description', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.course_id'], ),
    sa.PrimaryKeyConstraint('program_id')
    )
    op.create_table('exam',
    sa.Column('exam_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.Column('semester_id', sa.Integer(), nullable=True),
    sa.Column('exam_datetime', sa.TIMESTAMP(), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['course.course_id'], ),
    sa.ForeignKeyConstraint(['semester_id'], ['semester.semester_id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teacher.teacher_id'], ),
    sa.PrimaryKeyConstraint('exam_id')
    )
    op.create_table('homework',
    sa.Column('homework_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=True),
    sa.Column('deadline', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.course_id'], ),
    sa.PrimaryKeyConstraint('homework_id')
    )
    op.create_table('schedule',
    sa.Column('schedule_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.Column('building_id', sa.Integer(), nullable=True),
    sa.Column('classroom_id', sa.Integer(), nullable=True),
    sa.Column('day_of_week', sa.String(length=10), nullable=False),
    sa.Column('start_time', sa.Time(), nullable=False),
    sa.Column('end_time', sa.Time(), nullable=False),
    sa.ForeignKeyConstraint(['building_id'], ['building.building_id'], ),
    sa.ForeignKeyConstraint(['classroom_id'], ['classroom.classroom_id'], ),
    sa.ForeignKeyConstraint(['course_id'], ['course.course_id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teacher.teacher_id'], ),
    sa.PrimaryKeyConstraint('schedule_id')
    )
    op.create_table('studentgroup',
    sa.Column('group_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=10), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.course_id'], ),
    sa.PrimaryKeyConstraint('group_id')
    )
    op.create_index(op.f('ix_studentgroup_group_id'), 'studentgroup', ['group_id'], unique=False)
    op.create_table('curriculum',
    sa.Column('curriculum_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.Column('program_id', sa.Integer(), nullable=True),
    sa.Column('semester_number', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['department.department_id'], ),
    sa.ForeignKeyConstraint(['program_id'], ['courseprogram.program_id'], ),
    sa.PrimaryKeyConstraint('curriculum_id')
    )
    op.create_table('student',
    sa.Column('student_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=False),
    sa.Column('last_name', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.Column('phone_number', sa.String(length=12), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['studentgroup.group_id'], ),
    sa.PrimaryKeyConstraint('student_id')
    )
    op.create_table('grade',
    sa.Column('grade_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('grade', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.course_id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.student_id'], ),
    sa.PrimaryKeyConstraint('grade_id')
    )
    op.create_index(op.f('ix_grade_grade_id'), 'grade', ['grade_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_grade_grade_id'), table_name='grade')
    op.drop_table('grade')
    op.drop_table('student')
    op.drop_table('curriculum')
    op.drop_index(op.f('ix_studentgroup_group_id'), table_name='studentgroup')
    op.drop_table('studentgroup')
    op.drop_table('schedule')
    op.drop_table('homework')
    op.drop_table('exam')
    op.drop_table('courseprogram')
    op.drop_index(op.f('ix_teacher_teacher_id'), table_name='teacher')
    op.drop_table('teacher')
    op.drop_index(op.f('ix_course_course_id'), table_name='course')
    op.drop_table('course')
    op.drop_index(op.f('ix_department_department_id'), table_name='department')
    op.drop_table('department')
    op.drop_table('classroom')
    op.drop_table('semester')
    op.drop_index(op.f('ix_faculty_faculty_id'), table_name='faculty')
    op.drop_table('faculty')
    op.drop_table('building')
    # ### end Alembic commands ###
