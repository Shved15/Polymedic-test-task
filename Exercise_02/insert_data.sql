-- Insert data inside tables
INSERT INTO Faculty (name)
VALUES
('Math faculty'),
('Faculty of Philology');

INSERT INTO Department (name, faculty_id)
VALUES
('Math department', 1),
('department of Russian language and literature', 2);


INSERT INTO Course (name, department_id)
VALUES
('Math', 1),
('Russian', 2);

INSERT INTO StudentGroup (name, course_id)
VALUES
	('Group 1', 1),
	('Group 2', 1),
	('Group 3', 2);

INSERT INTO Student (first_name, last_name, email, phone_number, group_id)
VALUES
    ('John', 'Snow', 'john@example.com', '1234567890', 1),
    ('Matt', 'Deiv', 'matt@example.com', '9876543210', 1),
    ('Ann', 'Smoke', 'ann@example.com', '5678901234', 3),
    ('Kevin', 'Brown', 'kevin@example.com', '4321098765', 2),
    ('Alex', 'Smith', 'alex@example.com', '9012345678', 3);

INSERT INTO Teacher (first_name, last_name, email, phone_number, department_id)
VALUES
    ('Elis', 'Nikson', 'elis@example.com', '1234567890', 1),
    ('Maria', 'Deutch', 'maria@example.com', '9876543210', 1),
    ('Jess', 'Nol', 'jess@example.com', '5678901234', 2);


INSERT INTO Building (name, address)
VALUES
    ('№1', 'Address №1'),
    ('№2', 'Address №2'),
	('№3', 'Address №3');


INSERT INTO Classroom (classroom_number, building_id)
VALUES
    ('A101', 1),
    ('B201', 3);


INSERT INTO Schedule (course_id, teacher_id, building_id, classroom_id, day_of_week, start_time, end_time)
VALUES
    (1, 1, 3, 1, 'Monday', '09:00', '10:30'),
    (1, 2, 3, 2, 'Tuesday', '14:00', '15:30');


INSERT INTO Homework (course_id, title, description, created_at, deadline)
VALUES (1, 'Homework 1', 'Complete exercises 1-10',  '2021-05-30', '2022-05-31');
