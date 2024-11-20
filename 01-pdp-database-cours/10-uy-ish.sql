SELECT Track.Name AS TrackName, Album.Title AS AlbumName
FROM Track
LEFT JOIN Album ON Track.AlbumId = Album.AlbumId;

SELECT Track.Name AS TrackName, Genre.Name AS GenreName
FROM Track
LEFT JOIN Genre ON Track.GenreId = Genre.GenreId;

SELECT Customer.FirstName || ' ' || Customer.LastName AS CustomerName, SUM(Invoice.Total) AS TotalSpent
FROM Customer
LEFT JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
GROUP BY Customer.CustomerId;


SELECT Album.Title AS AlbumName, COUNT(Track.TrackId) AS TrackCount
FROM Album
LEFT JOIN Track ON Album.AlbumId = Track.AlbumId
GROUP BY Album.AlbumId;

SELECT Genre.Name AS GenreName, SUM(Track.UnitPrice) AS TotalCost
FROM Genre
LEFT JOIN Track ON Genre.GenreId = Track.GenreId
GROUP BY Genre.GenreId;

SELECT Customer.FirstName || ' ' || Customer.LastName AS CustomerName, MAX(Invoice.Total) AS MaxInvoice
FROM Customer
LEFT JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
GROUP BY Customer.CustomerId;

SELECT Customer.FirstName || ' ' || Customer.LastName AS CustomerName, MAX(Invoice.InvoiceDate) AS LastInvoiceDate
FROM Customer
LEFT JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
GROUP BY Customer.CustomerId;

SELECT Track.Name AS TrackName, SUM(InvoiceLine.Quantity) AS TotalSold
FROM Track

LEFT JOIN InvoiceLine ON Track.TrackId = InvoiceLine.TrackId
GROUP BY Track.TrackId;

SELECT Invoice.InvoiceId AS InvoiceID, COUNT(InvoiceLine.TrackId) AS TrackCount
FROM Invoice
LEFT JOIN InvoiceLine ON Invoice.InvoiceId = InvoiceLine.InvoiceId
GROUP BY Invoice.InvoiceId;

SELECT Employee.FirstName || ' ' || Employee.LastName AS SalespersonName, COUNT(Customer.CustomerId) AS CustomerCount
FROM Employee
LEFT JOIN Customer ON Employee.EmployeeId = Customer.SupportRepId
GROUP BY Employee.EmployeeId;
