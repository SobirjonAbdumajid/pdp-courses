-- CREATE TABLE students (
--     student_id SERIAL PRIMARY KEY,
--     name VARCHAR(100),
--     age INT
-- );

-- CREATE TABLE courses (
--     course_id SERIAL PRIMARY KEY,
--     course_name VARCHAR(100),
--     credit_hours INTEGER
-- );

-- CREATE TABLE enrollments (
--     enrollment_id SERIAL PRIMARY KEY,
--     student_id INTEGER REFERENCES students(student_id),
--     course_id INTEGER REFERENCES courses(course_id),
--     grade INTEGER
-- );


-- INSERT INTO students (name, age)
-- VALUES
-- ('Alice', 20),
-- ('Bob', 22),
-- ('Charlie', 19),
-- ('Diana', 21);


-- INSERT INTO courses (course_name, credit_hours)
-- VALUES
-- ('Mathematics', 3),
-- ('History', 3),
-- ('Physics', 4),
-- ('Art', 2),
-- ('Science', 4),
-- ('English', 3),
-- ('Biology', 4),
-- ('Chemistry', 4),
-- ('Geography', 3),
-- ('Computer Science', 3);


-- INSERT INTO enrollments (student_id, course_id, grade)
-- VALUES
-- (1, 1, 5),
-- (1, 2, 4),
-- (2, 3, 3),
-- (2, 4, 5),
-- (3, 5, 4),
-- (4, 1, 3),
-- (5, 2, 2),
-- (3, 4, 5),
-- (4, 5, 3),
-- (1, 3, 4),
-- (2, 5, 5),
-- (5, 6, 3),
-- (1, 7, 4),
-- (2, 8, 5),
-- (3, 9, 2),
-- (4, 10, 4),
-- (5, 3, 5),
-- (1, 4, 4),
-- (2, 6, 5),
-- (3, 7, 3),
-- (4, 8, 2),
-- (5, 9, 4),
-- (1, 10, 5),
-- (2, 1, 4),
-- (3, 2, 5),
-- (4, 3, 3),
-- (5, 4, 4),
-- (1, 5, 3),
-- (2, 7, 2),
-- (3, 8, 4);




-- select * from courses;

-- select * from enrollments;

-- select * from students;



