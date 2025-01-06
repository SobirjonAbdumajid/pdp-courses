select * from `kreditbank dataset`;

-- 1. nechta mijozning ma'lumoti university.degree darajasida?
select count(*)
from `kreditbank dataset`
where education = 'university.degree';

-- 2. qarzi bor mijozlar uchun duration'ning o'rtacha qiymati qancha?
select avg(duration)
from `kreditbank dataset`
where loan = 'yes';

-- 3. eng ko'p mijozlar necha yoshda?
select age, count(*) as mijoz_soni
from `kreditbank dataset`
group by age
order by count(*) desc;

-- 4. nechta erkak mijozning uy uchun qarzi bor?
select count(*)
from `kreditbank dataset`
where gender = 'male' and housing = 'yes';

-- 5. nechta ayol ustozning ma'lumoti university.degree darajasida?
select count(*)
from `kreditbank dataset`
where gender = 'female' and job = 'teacher' and education = 'university.degree';
