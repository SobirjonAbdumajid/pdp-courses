-- 1
create database university_db;

-- 2
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birthdate DATE,
    enrollment_year INTEGER
);

-- 3
INSERT INTO students (first_name, last_name, birthdate, enrollment_year) VALUES
('Alice', 'Smith', '2002-05-14', 2020),
('Bob', 'Johnson', '2001-07-23', 2011),
('Charlie', 'Williams', '2003-01-10', 2021),
('David', 'Brown', '2000-08-30', 2018),
('Emma', 'Jones', '2002-11-25', 2000),
('Fiona', 'Garcia', '2001-03-17', 2019),
('George', 'Martinez', '2003-09-12', 2021),
('Hannah', 'Rodriguez', '2002-12-05', 2020),
('Ivan', 'Davis', '2001-06-21', 2019),
('Jessica', 'Lopez', '2003-10-09', 2021),
('Kevin', 'Gonzalez', '2000-04-18', 2018),
('Laura', 'Wilson', '2002-02-22', 2020),
('Michael', 'Anderson', '2001-05-19', 2009),
('Nina', 'Thomas', '2003-07-27', 2021),
('Oliver', 'Taylor', '2002-08-08', 2020),
('Paula', 'Moore', '2001-01-11', 2019),
('Quincy', 'Jackson', '2003-02-20', 2021),
('Rachel', 'Martin', '2002-06-16', 2010),
('Steve', 'Lee', '2000-09-29', 2018),
('Tina', 'Perez', '2001-11-15', 2019);

-- 4
select * from students;

-- 5
SELECT * FROM students WHERE enrollment_year > 2017;

-- 6
select enrollment_year, count(enrollment_year) 
from students 
group by enrollment_year
order by enrollment_year;
