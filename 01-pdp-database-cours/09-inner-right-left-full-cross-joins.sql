-- select * from employee;

-- create table city(
-- 	id serial primary key,
-- 	name varchar(50)
-- );

-- create table students (
-- 	id serial primary key,
-- 	name varchar(100),
-- 	city_id int references city(id)
-- );

-- insert into city(name)
-- values
-- ('Toshkent'),
-- ('Buxoro'),
-- ('Namangan'),
-- ('Jizzax');


-- insert into students(name, city_id)
-- values
-- ('Sobirjon', 1),
-- ('Sardorbek', 2),
-- ('Abbos', 2),
-- ('Anna', Null);


-- -- inner join
-- select students.name, city.name
-- from students
-- inner join city on students.city_id = city.id; 

-- -- left join
-- select students.name, city.name
-- from students
-- left join city on students.city_id = city.id;

-- -- right join
-- select students.name, city.name
-- from students
-- right join city on students.city_id = city.id;

-- -- full join
-- explain analyze
-- select students.name, city.name
-- from students
-- full join city on students.city_id = city.id;

-- -- cross join
-- select students.name, city.name
-- from students
-- cross join city;

-- -- other way to inner join
-- explain analyze
-- select *
-- from students
-- where city_id in (select id from city);




CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT
);

CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100),
    student_id INT REFERENCES students(student_id)
);

INSERT INTO students (name, age)
VALUES
('Alice', 20),
('Bob', 22),
('Charlie', 19),
('Diana', 21);

INSERT INTO courses (course_name, student_id)
VALUES
('Math', 1),
('History', 1),
('Science', 2),
('Art', 3),
('Math', NULL);


select * from students;
select * from courses;

-- 1
select students.name, courses.course_name
from courses
RIGHT join students on courses.student_id = students.student_id;

-- 2
select students.name, courses.course_name
from courses
left join students on courses.student_id = students.student_id
where name is Null;

-- 3
select students.name, count(courses.course_id)
from courses
right join students on courses.student_id = students.student_id
group by students.name;

-- 4
select distinct students.name, students.age
from courses
left join students on courses.student_id = students.student_id
where age < 21





