# Subquery Basics (World Database)

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
select name
from country
where surfacearea>(select avg(surfacearea) from country);

# 5
select name
from country
where lifeexpectancy > (select avg(lifeexpectancy) from country);


# World Database: Any and All Operators
-- 1. Find countries whose population is greater than the population of all cities
SELECT name, population
FROM country
WHERE population > ALL (SELECT population FROM city);

-- 2. Find countries with the minimum population
SELECT name, population
FROM country
WHERE population = (SELECT MIN(population) FROM country);

-- 3. Find the highest life expectancy in Asia
SELECT MAX(lifeexpectancy)
FROM country
WHERE continent = 'Asia';

-- 4. Find the minimum life expectancy for each continent
SELECT continent, MIN(lifeexpectancy) AS min_life_expectancy
FROM country
GROUP BY continent;

-- 5. Find the country with the smallest surface area in each continent
select continent, name, SurfaceArea
from country
where (continent, surfacearea) in (
	select continent, min(surfacearea)
    from country
    group by continent
);


-- 6. Find countries with a population greater than or equal to the average population in their region
SELECT name, region, population
FROM country
WHERE population >= (SELECT AVG(population) FROM country AS c2 WHERE country.region = c2.region);

-- 7. Find the country with the smallest surface area
SELECT name, surfacearea
FROM country
WHERE surfacearea = (SELECT MIN(surfacearea) FROM country);

-- 8. List countries with a life expectancy greater than the world average life expectancy
SELECT name, lifeexpectancy
FROM country
WHERE lifeexpectancy > (SELECT AVG(lifeexpectancy) FROM country);

-- 9. Find the city with the smallest population in each region
SELECT region, name, population
FROM city
WHERE (region, population) IN (
    SELECT region, MIN(population)
    FROM city
    GROUP BY region
);

-- 10. Find countries with an area smaller than any country in their region
SELECT name, surfacearea
FROM country AS c1
WHERE surfacearea < ANY (SELECT surfacearea FROM country AS c2 WHERE c1.region = c2.region AND c1.code <> c2.code);
























