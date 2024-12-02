-- CREATE TABLE students (
--     student_id SERIAL PRIMARY KEY,
--     name VARCHAR(100),
--     birth_date DATE,
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
-- ('Sardorbek', 22),
-- ('Alice', 20),
-- ('Bob', 22),
-- ('Charlie', 19),
-- ('Diana', 21),
-- ('Sobirjon', 19);

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


-- -- 3.1. Queries
-- 1
SELECT name, age, birth_date
FROM students;

-- 2
select students.name, courses.course_name
from students
join enrollments on students.student_id = enrollments.student_id
join courses on enrollments.course_id = courses.course_id
where courses.course_name = 'Mathematics';

-- 3
select students.name, avg(enrollments.grade)
from enrollments
join courses on enrollments.course_id = courses.course_id
join students on enrollments.student_id = students.student_id
group by students.name
having avg(enrollments.grade) < 4;

-- -- 3.2. Joining data (JOIN)
-- 1
select students.name, courses.course_name
from enrollments
join students on enrollments.student_id = students.student_id
join courses on enrollments.course_id = courses.course_id
order by students.name;

-- 2
SELECT students.name
FROM students
LEFT JOIN enrollments ON students.student_id = enrollments.student_id
WHERE enrollments.student_id IS NULL;

-- -- 3.3. Grouping and Aggregates
-- 1
SELECT courses.course_name, COUNT(enrollments.student_id) AS student_count
FROM courses
LEFT JOIN enrollments ON courses.course_id = enrollments.course_id
GROUP BY courses.course_name;

-- 2
SELECT courses.course_name, COUNT(enrollments.student_id) AS student_count
FROM courses
JOIN enrollments ON courses.course_id = enrollments.course_id
GROUP BY courses.course_name
ORDER BY student_count DESC
LIMIT 1;

-- -- 3.4. Filtering and Sorting
-- 1
SELECT name
FROM students
ORDER BY name;

-- 2
SELECT students.name
FROM students
JOIN enrollments ON students.student_id = enrollments.student_id
JOIN courses ON enrollments.course_id = courses.course_id
WHERE courses.course_name = 'History' AND enrollments.enrollment_date > '2015-01-01';

-- -- 3.5. Working with Subqueries
-- 1
SELECT students.name
FROM students
JOIN enrollments ON students.student_id = enrollments.student_id
GROUP BY students.student_id
HAVING COUNT(enrollments.course_id) > (
    SELECT AVG(course_count)
    FROM (
        SELECT COUNT(enrollments.course_id) AS course_count
        FROM enrollments
        GROUP BY enrollments.student_id
    ) AS avg_course_counts
);

-- 2
SELECT courses.course_name
FROM courses
JOIN enrollments ON courses.course_id = enrollments.course_id
WHERE enrollments.student_id = (
    SELECT student_id
    FROM enrollments
    GROUP BY student_id
    ORDER BY AVG(grade)
    LIMIT 1
);

-- -- 3.6. Modifying Data
-- 1
UPDATE enrollments
SET grade = 3
WHERE grade = 4;

-- 2
DELETE FROM students
WHERE student_id NOT IN (SELECT DISTINCT student_id FROM enrollments);

-- 3
INSERT INTO students (name, age, birth_date)
VALUES ('New Student', 20, '2004-01-01');

INSERT INTO enrollments (student_id, course_id, grade)
VALUES 
    ((SELECT student_id FROM students WHERE name = 'New Student'), 1, 5),
    ((SELECT student_id FROM students WHERE name = 'New Student'), 2, 4);


