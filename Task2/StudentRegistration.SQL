/* Student Table */
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100)
);

/* Courses Table */
CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    course_code VARCHAR(20),
    instructor VARCHAR(100)
);

/* Registration Table */ 
CREATE TABLE Registrations (
    registration_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    registration_date DATE,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- Retiving all students registered for a specific course
SELECT * FROM Students
JOIN Registrations ON Students.student_id = Registrations.student_id
JOIN Courses ON Registrations.course_id = Courses.course_id
WHERE Courses.course_name = '<specific course name>';

--Get the details of a student's course registrations, including the course name and instructor.
SELECT Students.first_name, Students.last_name, Courses.course_name, Courses.instructor
FROM Students
JOIN Registrations ON Students.student_id = Registrations.student_id
JOIN Courses ON Registrations.course_id = Courses.course_id
WHERE Students.student_id = <student_id>;

-- Find the course with no registered students 
SELECT Courses.course_name, Courses.course_code, Courses.instructor 
FROM Courses
LEFT JOIN Registrations ON Courses.course_id = Registrations.course_id
WHERE Registrations.registration_id IS NULL;

-- Inserting New student in DB 
INSERT INTO Students (first_name, last_name, email)
VALUES ('ram', 'prashad', 'ram@email.com');

-- Adding New Course in DB
INSERT INTO Courses (course_name, course_code, instructor)
VALUES ('Course11', 'CS101', 'Instructor1');

-- Register a student for a course:
INSERT INTO Registrations (student_id, course_id, registration_date)
VALUES (<student_id>, <course_id>, '2023-01-01');

-- Remove Student From Course 
DELETE FROM Registrations
WHERE student_id = <student_id> AND course_id = <course_id>;





