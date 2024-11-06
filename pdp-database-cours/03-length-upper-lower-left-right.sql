#STRING FUNCTIONS (Length, Upper, lower, left, right)
#1
select FirstName, PostalCode, LENGTH(PostalCode) AS PostalCodeLength from customer;
#2
select BillingPostalCode, length(BillingPostalCode) as BPC from invoice;
#3
select upper(BillingCountry), upper(BillingCity) from invoice;
#4
select lower(BillingAddress) from invoice;
#5
select Phone, upper(FirstName), upper(LastName), lower(Address) from customer where Phone like '+3%';
#6
select upper(FirstName), upper(Country), Phone, Email, SupportRepId  from customer order by SupportRepId desc;
#7
select LastName, HireDate from employee;
#8
select LastName, BirthDate from employee;
#9
UPDATE Employee
SET Email = REPLACE(Email, '.fr', '.com')
WHERE Email LIKE '%.fr';
#10
SELECT 
    CONCAT(FirstName, ' ', UPPER(LastName)) AS FullName
FROM 
    Employee;
#11
select     CONCAT(BirthDate, ' ', UPPER(FirstName)) AS Fullcatalog from employee;
#12
select BirthDate, FirstName, length(  CONCAT(BirthDate, ' ', UPPER(FirstName)) )AS Fullcatalog from employee;
