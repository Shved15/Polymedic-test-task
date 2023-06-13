-- Выбрать всех студентов, обучающихся на курсе "Математика".

SELECT student.student_id, student.first_name, student.last_name
FROM student
JOIN studentgroup ON student.group_id = studentgroup.group_id
JOIN course ON studentgroup.course_id = course.course_id
WHERE course.name = 'Math';



-- Обновить оценку студента по курсу.

UPDATE Grade
SET grade = 4
WHERE student_id = 1 AND course_id = 1;


-- Выбрать всех преподавателей, которые преподают в здании №3.

SELECT DISTINCT Teacher.*
FROM Teacher
JOIN Department ON Department.department_id = Teacher.department_id
JOIN Schedule ON Schedule.teacher_id = Teacher.teacher_id
JOIN Building ON Building.building_id = Schedule.building_id
WHERE Building.name = '№3';


-- Удалить задание для самостоятельной работы, которое было создано более года назад.

DELETE FROM Homework
WHERE created_at < (CURRENT_DATE - INTERVAL '1 year');


-- Добавить новый семестр в учебный год.

INSERT INTO Semester (semester_id, name, start_date, end_date)
VALUES (6, 'Autumn semester', '2023-09-01', '2023-12-31');
