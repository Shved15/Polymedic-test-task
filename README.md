# Polymedic-test-task

## Project Description:
The project is a RESTful API for managing university. It allows creating, retrieving, updating, and deleting data about students, teachers, courses, and grades.

## Installation and Setup Instructions:

1. Install Docker or docker desktop if it is not already installed.
2. Clone rep
```bash
git clone https://github.com/Shved15/Polymedic-test-task.git
cd Polymedic-test-task
```
4. Create the .env  file and configure the database connection parameters just like .env-sample file.

5. Inside the project directory run the command:
```bash
docker-compose up --build
```

6. The application will be available at http://localhost:8000.


API Usage Instructions:

- Using the API can be done either using the Postman or Insomnia services or by accessing the following addresses: http://localhost:8000/docs/ or http://localhost:8000/redoc/.
- To create a student, send a POST request to /students with the student data in the request body.
- To retrieve student information by ID, send a GET request to /students/{student_id}.
- To update student information by ID, send a PUT request to /students/{student_id} with the updated student data in the request body.
- To delete a student by ID, send a DELETE request to /students/{student_id}.
- To retrieve a list of teachers, send a GET request to /teachers.
- To create a course, send a POST request to /courses with the course data in the request body.
- To retrieve course information by ID, send a GET request to /courses/{course_id}.
- To retrieve a list of students in a course by course ID, send a GET request to /courses/{course_id}/students.
- To create a grade, send a POST request to /grades with the grade data in the request body.
- To update a grade by ID, send a PUT request to /grades/{grade_id} with the updated grade data in the request body.



# Task
Задание для кандидата на должность Junior Python Developer

Целью этого задания является разработка структуры базы данных и реализация API для "Системы управления университетом". Это система, где учитываются студенты, преподаватели, курсы, группы, отделения университета, оценки и другие соответствующие данные.

1. База данных

Сначала вам необходимо создать схему базы данных, состоящую из 15 сущностей:
- Студент
- Преподаватель
- Курс
- Группа
- Отделение
- Оценка
- Расписание
- Здание
- Аудитория
- Семестр
- Факультет
- Экзамен
- Задание для самостоятельной работы
- Программа курса
- Учебный план
- 
Ваша задача - создать ER-диаграмму (схему связей между сущностями) и определить свойства каждой из этих сущностей. Затем напишите SQL запросы для создания соответствующих таблиц, включающих все необходимые поля и связи между ними.
Мы ждём от вас:
ER-диаграмму, которая описывает все сущности и связи между ними.
SQL скрипт, который создаёт все таблицы с полями, их типами данных, ключами и связями.
Краткое описание каждой сущности и её свойств.

2. SQL запросы

Пожалуйста, реализуйте следующие SQL запросы:
- Выбрать всех студентов, обучающихся на курсе "Математика".
- Обновить оценку студента по курсу.
- Выбрать всех преподавателей, которые преподают в здании №3.
- Удалить задание для самостоятельной работы, которое было создано более года назад.
- Добавить новый семестр в учебный год.

3. FastAPI

Мы бы хотели увидеть следующие точки входа API:
- POST /students - создать нового студента.
- GET /students/{student_id} - получить информацию о студенте по его id.
- PUT /students/{student_id} - обновить информацию о студенте по его id.
- DELETE /students/{student_id} - удалить студента по его id.
- GET /teachers - получить список всех преподавателей.
- POST /courses - создать новый курс.
- GET /courses/{course_id} - получить информацию о курсе по его id.
- GET /courses/{course_id}/students - получить список всех студентов на курсе.
- POST /grades - создать новую оценку для студента по курсу.
- PUT /grades/{grade_id} - обновить оценку студента по курсу.
Ожидается реализация этих точек входа API с использованием FastAPI, включая входные и выходные модели Pydantic для каждого маршрута.

4. Публикация и документация

Загрузите свой код в публичный репозиторий на GitHub и предоставьте ссылку на него. Включите в README файл:
- Описание проекта.
- Инструкции по установке и запуску вашего приложения.
- Инструкции по использованию API.
