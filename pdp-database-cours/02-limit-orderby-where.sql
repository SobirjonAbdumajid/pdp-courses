# MASALALAR: (limit, order by, where)
#1
select * from track limit 5;
#2
select * from album limit 10;
#3
select FirstName, LastName from customer limit 5;
#4
select Name, UnitPrice from track order by UnitPrice;
#5
select * from album ;
#6 
select InvoiceDate from invoice order by(InvoiceDate) desc limit 5;
#7
select Name, Milliseconds  from track order by Milliseconds desc;
#8
select FirstName, Country from customer where Country='Canada';
#9
select * from track where Milliseconds > 200000;
#10
select * from customer where Country='USA';
#11
select * from track where UnitPrice > 0.99;
#12
select * from invoice where InvoiceDate > 2010-01-01;

