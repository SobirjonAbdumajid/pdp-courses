# like, order by, limit, Aliasing,
select * from country;

select * from country where capital like '__%';
select * from country order by Population;
select * from country order by Population desc limit 3;
select  name, name  as 'nom' from country;

#like
#1
select * from country where name like 'A%';
#2
select IndepYear     from country where (IndepYear like '%1' and  Region like 'A%' or Region like 'B%');
#3
select LifeExpectancy from country where LifeExpectancy like '7%';
#4
select Name, IndepYear, Capital  from country where Capital like '__' ;
#5
select address_id, phone, postal_code from address where postal_code like '5%' and phone like '%5';

#order by clause
#1
select Name, Population from country order by Population;
#2
select Code, Population from country order by Population;
#3
select * from city order by Population desc;
#4 
select Name, LifeExpectancy, Population from country where Continent = 'Asia' order by Population desc;
#5
select Name, Capital,IndepYear, Population from country where Continent = 'Europe' and Capital like '___' order by Population desc;


#limit 
#1
select * from country limit 7;
#2
select Name, LifeExpectancy, Population  from country order by Population limit 5;
#3 
select Name, Population from country where Continent = 'Asia'  order by  Population limit 3;
#4
select Name, SurfaceArea, Continent from country where Continent = 'Africa' order by SurfaceArea desc limit 10;
#5
select Name, Continent, GNP, IndepYear, LifeExpectancy from country where Continent = 'Europe' and IndepYear > 1950 and LifeExpectancy >70 order by GNP limit 5;

#alliasing
#1
select * from category;
SELECT category_id AS ID,  name AS names FROM category;
#2
select category_id +100 as new_id, last_update as updates from category ;
#3
select GenreId as ID, Name as Genre_name from genre;
#4
select InvoiceId ,(UnitPrice*Quantity) as revenue from invoiceline;
#5
select CustomerId+100 as ID, FirstName as Forename, LastName as surname from customer ;




