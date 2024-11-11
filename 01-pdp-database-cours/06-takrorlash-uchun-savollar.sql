# Takrorlash uchun savollar

select * from country;

# 1
select region, count(name) from country where name like '%land%' group by region with rollup;

# 2
select continent, count(name) from country where length(name) < 5 group by continent with rollup;

# 3
select  region, reverse(name), count(*) from country group by region, reverse(name);

# 4
select region, count(name),
case
when name like 'United%' then 'Birlashgan'
else 'turli' end as name_status
from country
group by region, name_status;

# 5
select region, count(name) 
from country 
where length(name) > 10 or indepyear > 1900 
group by region 
order by count(*) desc;

# 6
select continent, count(name) from country where name like '%stan' group by continent;

















