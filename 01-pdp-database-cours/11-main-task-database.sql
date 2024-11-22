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
SELECT 
    Track.Name AS TrackName,
    SUM(InvoiceLine.UnitPrice * InvoiceLine.Quantity) AS TotalAmountSold
FROM 
    Track
LEFT JOIN 
    InvoiceLine ON Track.TrackId = InvoiceLine.TrackId
GROUP BY 
    Track.TrackId;



SELECT 
    Invoice.InvoiceId AS InvoiceName,
    COUNT(InvoiceLine.TrackId) AS NumberOfTracks
FROM 
    Invoice
LEFT JOIN 
    InvoiceLine ON Invoice.InvoiceId = InvoiceLine.InvoiceId
GROUP BY 
    Invoice.InvoiceId;



SELECT 
    Employee.FirstName || ' ' || Employee.LastName AS SalespersonName,
    COUNT(Customer.CustomerId) AS NumberOfCustomers
FROM 
    Employee
LEFT JOIN 
    Customer ON Employee.EmployeeId = Customer.SupportRepId
GROUP BY 
    Employee.EmployeeId;
