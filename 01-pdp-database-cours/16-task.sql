-- Clean employees table
ALTER TABLE employees RENAME COLUMN `_<>employee_id` TO employee_id;
ALTER TABLE employees RENAME COLUMN `phone_NUMBER` TO phone;
ALTER TABLE employees RENAME COLUMN `salary$$$` TO salary;

select * from employees;

update employees
set phone=regexp_replace(phone, '[()/<>=+-]', '');

UPDATE employees
SET department = CONCAT(UPPER(LEFT(department, 1)), LOWER(SUBSTRING(department, 2)));

update employees
set phone=concat(substring(phone,1,3),'-',substring(phone, 4,3),'-', substring(phone,7));

UPDATE employees
SET first_name = CONCAT(UPPER(LEFT(first_name, 1)), LOWER(SUBSTRING(first_name, 2))),
    last_name = CONCAT(UPPER(LEFT(last_name, 1)), LOWER(SUBSTRING(last_name, 2)));
    
update employees
set department = CONCAT(UPPER(LEFT(department, 1)), LOWER(SUBSTRING(department, 2)));

SELECT * FROM employees;
