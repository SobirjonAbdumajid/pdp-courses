create or replace view student_view as
	select * from students
	where birth_date > '2000-01-01'
	with local check option;

select * from student_view;

insert into student_view (name, birth_date, age, enrollment_year)
values ('Umar', '2012-01-01', 26, 2017);

select * from students;
select * from enrollments;

create function update_student_name() returns void as $$
        update students
        set name = 'Sobirxon'
        where name = 'Sobirjon'
    $$ language sql;

select update_student_name();

create or replace function get_sum_price() returns float8 as $$
        select sum(price) from holiday
    $$ language sql;

select get_sum_price();


create or replace function get_avg_price() returns float8 as $$
        select avg(price) from holiday
    $$ language sql;

select get_avg_price();

create or replace function get_country_with_avg_price() returns TABLE(destination_country TEXT, avg_price NUMERIC) as $$
        select destination_country, avg(price) from holiday
        group by destination_country;
    $$ language sql;

select *
from holiday;


CREATE OR REPLACE FUNCTION get_country_with_avg_price() RETURNS TABLE(destination_country TEXT, avg_price NUMERIC) AS $$
    SELECT destination_country, AVG(price)
    FROM holiday
    GROUP BY destination_country;
$$ LANGUAGE sql;

select get_country_with_avg_price();


create or replace function example(country varchar) returns setof double precision as $$
        select price from holiday
        where destination_country = country;
    $$ language sql;

create or replace function example2(country varchar) returns double precision as $$
        select price from holiday
        where destination_country = country;
    $$ language sql;

create or replace function example3(country varchar default 'Uzbekistan', out double precision) as
$$
    select price from holiday
    where destination_country = country;
$$ language sql;


create or replace function example4(min_price double precision, country varchar default 'Uzbekistan')
    returns setof double precision as
$$
    select price
    from holiday
    where destination_country = country
    and price > min_price;
$$ language sql;


select * from example('Uzbekistan');
select * from example2('Uzbekistan');
select * from example3('Russia');
select * from example3();
select * from example4(400);


select destination_country
from holiday;

-- ---------------------- i ---------------------- --


create or replace function example5(limit_of double precision, country varchar)
    returns setof double precision as
$$
    select destination_country, price
    from holiday
    where destination_country = country
    order by price desc
    limit limit_of;
$$ language sql;



create or replace function example6(limit_of double precision, country varchar)
    returns TABLE(destination_country varchar, price double precision) as
$$
    select destination_country, price
    from holiday
    where destination_country = country
    order by price desc
    limit limit_of;
$$ language sql;


create or replace function example7(limit_of double precision, country varchar)
    returns setof holiday as
$$
    select destination_country, price
    from holiday
    where destination_country = country
    order by price desc
    limit limit_of;
$$ language sql;

select * from example6(10, 'Russia');


CREATE OR REPLACE FUNCTION example8(
    limit_of double precision,
    country varchar
)
RETURNS SETOF holiday AS $$
    SELECT *
    FROM holiday
    WHERE destination_country = country
    ORDER BY price DESC
    LIMIT limit_of;
$$ LANGUAGE sql;

select * from example8(10, 'Russia');


CREATE TYPE holiday_price AS (
    destination_country varchar,
    price double precision
);

CREATE OR REPLACE FUNCTION example10(
    limit_of double precision,
    country varchar
)
RETURNS SETOF holiday_price AS $$
    SELECT destination_country, price
    FROM holiday
    WHERE destination_country = country
    ORDER BY price DESC
    LIMIT limit_of;
$$ LANGUAGE sql;

select * from example10(10, 'Russia');


create or replace function perimeter(a int, b int, c int) returns int as
$$
    declare
        perimeter integer;
    begin
        perimeter = a + b + c;
        return perimeter;
    end;
$$ language plpgsql;

select perimeter(2,3,4);



create or replace function min_max_price() returns setof holiday as
$$
    declare
        avg_price int;
        min_price int;
        max_price int;
    begin
        select avg(price) into avg_price from holiday;
        min_price := avg_price * 0.75;
        max_price := avg_price * 1.25;

        return query select * from holiday
        where price between min_price and max_price;
    end;
$$ language plpgsql;

select * from min_max_price();