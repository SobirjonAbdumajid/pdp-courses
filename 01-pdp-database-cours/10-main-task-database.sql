# 1
select * from album;
select * from track;
select * from genre;
select track.Name, album.Title
from track
left join album on track.AlbumId = album.AlbumId;

# 2
select track.name, genre.Name
from track
left join genre on track.GenreId = genre.GenreId;

# 3
select * from customer;
select * from invoice;
select customer.FirstName, sum(invoice.Total)
from invoice
left join customer on invoice.CustomerId = customer.CustomerId
group by customer.FirstName;


# 4
select * from album;
select * from track;
select album.Title, count(track.TrackId)
from album
left join track on album.AlbumId = track.AlbumId
group by album.Title;



# 5
select * from track;
select * from genre;
select genre.Name, sum(track.UnitPrice)
from genre
left join track on genre.GenreId = track.GenreId
group by genre.name;


# 6
select * from invoice;
select * from customer;
select customer.FirstName, max(invoice.Total)
from customer
left join invoice on customer.CustomerId = invoice.CustomerId
group by customer.FirstName;


# 7
select customer.FirstName, max(invoice.InvoiceDate)
from customer
left join invoice on customer.CustomerId = invoice.CustomerId
group by customer.CustomerId;


# 8
select * from invoice;
select * from track;
select * from invoiceline;
select track.name, sum(invoiceline.UnitPrice * invoiceline.Quantity)
from track
left join invoiceline on track.TrackId = invoiceline.TrackId
group by track.Name;


# 9
select invoice.InvoiceId, count(invoiceline.TrackId)
from invoice
left join invoiceline on invoice.InvoiceId = invoiceline.InvoiceId
group by invoice.InvoiceId;


# 10
select * from customer;
select * from employee;
select employee.FirstName, count(customer.CustomerId)
from employee
left join customer on employee.EmployeeId = customer.SupportRepId
group by employee.EmployeeId;
