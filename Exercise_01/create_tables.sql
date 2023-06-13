-- Create Faculty table
CREATE TABLE Faculty (
    faculty_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Create Department table
CREATE TABLE Department (
    department_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
	faculty_id INT,
	FOREIGN KEY (faculty_id) REFERENCES Faculty(faculty_id)

);

-- Create Course Table
CREATE TABLE Course (
    course_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
	department_id INT,
    FOREIGN KEY (department_id) REFERENCES Department(department_id)
);

-- Create StudentGroup Table
CREATE TABLE StudentGroup (
    group_id SERIAL PRIMARY KEY,
    name VARCHAR(10) NOT NULL,
    course_id INT,
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

-- Create Student Table
CREATE TABLE Student (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
	email VARCHAR(30) NOT NULL,
	phone_number VARCHAR(12),
    group_id INT,
    FOREIGN KEY (group_id) REFERENCES StudentGroup(group_id)
);

-- Create Teacher Table
CREATE TABLE Teacher (
    teacher_id SERIAL PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
	last_name VARCHAR(30) NOT NULL,
	email VARCHAR(30) NOT NULL,
	phone_number VARCHAR(12) NOT NULL,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES Department(department_id)
);



-- Create Grade Table
CREATE TABLE Grade (
    grade_id SERIAL PRIMARY KEY,
    student_id INT,
    course_id INT,
    grade INT,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

-- Create Building table
CREATE TABLE Building (
    building_id SERIAL PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
	address VARCHAR(255) NOT NULL
);

-- Create Classroom table
CREATE TABLE Classroom (
    classroom_id SERIAL PRIMARY KEY,
    classroom_number VARCHAR(5) NOT NULL,
    building_id INT,
    FOREIGN KEY (building_id) REFERENCES Building(building_id)
);

-- Create Schedule table
CREATE TABLE Schedule (
    schedule_id SERIAL PRIMARY KEY,
    course_id INT,
    teacher_id INT,
    building_id INT,
    classroom_id INT,
	day_of_week VARCHAR(10) NOT NULL,
	start_time TIME NOT NULL,
	end_time TIME NOT NULL,
    FOREIGN KEY (course_id) REFERENCES Course(course_id),
    FOREIGN KEY (teacher_id) REFERENCES Teacher(teacher_id),
    FOREIGN KEY (building_id) REFERENCES Building(building_id),
    FOREIGN KEY (classroom_id) REFERENCES Classroom(classroom_id)
);

-- Create Semester table
CREATE TABLE Semester (
    semester_id SERIAL PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);



-- Create Exam table
CREATE TABLE Exam (
    exam_id SERIAL PRIMARY KEY,
    course_id INT,
    teacher_id INT,
	semester_id INT,
    exam_datetime TIMESTAMP,
	duration INT NOT NULL,
    FOREIGN KEY (course_id) REFERENCES Course(course_id),
    FOREIGN KEY (teacher_id) REFERENCES Teacher(teacher_id),
    FOREIGN KEY (semester_id) REFERENCES Semester(semester_id)

);

-- Create Homework table
CREATE TABLE Homework (
    homework_id SERIAL PRIMARY KEY,
    course_id INT,
	title VARCHAR(255) NOT NULL,
    description VARCHAR NOT NULL,
    created_at DATE,
    deadline DATE,
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

-- Create CourseProgram table
CREATE TABLE CourseProgram (
    program_id SERIAL PRIMARY KEY,
    course_id INT,
	module_number INT NOT NULL,
	module_title VARCHAR(128) NOT NULL,
    module_description TEXT,
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

-- Create Curriculum table
CREATE TABLE Curriculum (
    curriculum_id SERIAL PRIMARY KEY,
    department_id INT,
	program_id INT,
	semester_number INT,
	FOREIGN KEY (department_id) REFERENCES Department(department_id),
	FOREIGN KEY (program_id) REFERENCES CourseProgram(program_id)
);
