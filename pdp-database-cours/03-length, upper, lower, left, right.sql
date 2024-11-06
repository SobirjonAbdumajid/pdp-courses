#String functions (Length, Upper, lower, left, right, substring, replace, locate, concat)

#1
select BillingCity, LENGTH(BillingCity) from invoice;
#2
select BillingCity, LENGTH(BillingCity) as lengs_ba from invoice;
#3 
select  upper(name) from genre;
#4
select lower(name) as name from mediatype;
#5 
select PostalCode , upper(FirstName), upper(LastName), lower(City), Phone from customer where PostalCode like "9%";
#6
select BirthDate from employee;
#7
select *, replace(Email, 'ca', 'com') from customer;
#8
select   CONCAT(Upper(FirstName), ' ', UPPER(LastName)) as full_name from employee;
#9
select concat(upper(FirstName), ' ', BirthDate) as NBM from employee;
#10
select concat(name, ' ', IndepYear) as full from country;
#11
select Capital, upper(LocalName) from country where Capital between  10 and 99;
#12
select upper(Name),Population-1000 as population_in_k from country;
