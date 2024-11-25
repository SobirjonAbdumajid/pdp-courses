select * from city;
select * from country;

# 1
select name, Population
from country
where population=(select max(Population) from country);

# 2
select name, population
from country
where population>(select avg(population) from country);

# 3
select name
from country
where population<(select avg(population) from country);

# 4





























