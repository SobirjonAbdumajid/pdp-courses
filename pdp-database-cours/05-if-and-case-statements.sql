# if
# 1
select total, if (total<2, 'amazing', 'great') from invoice;

# 2
select total, if (total>10, 'yaxshi', 'yomon') from invoice order by total desc;

# 3
select Name, IndepYear, if (IndepYear<1900, 'old', 'new') as indep_status from country;

# 4
select total, if (total>=5, total*1.25, total*0.75) from invoice;

# 5
select total, if (total<=10, total*1.5, total*0.85) as result_total from invoice;






# Case Statements
# 1
select * from film;

# 2
select total, if (total>10, 'yaxshi', 'yomon') from invoice order by total desc;

# 3
select total, if (total>10, 'yaxshi', 'yomon') from invoice order by total desc;

# 4
select total, if (total>10, 'yaxshi', 'yomon') from invoice order by total desc;

# 5
select total, if (total>10, 'yaxshi', 'yomon') from invoice order by total desc;