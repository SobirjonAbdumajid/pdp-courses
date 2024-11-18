select * from artist;


# 1.	Chinook ma’lumotlar bazasidan Artist  jadvalidagi barcha musiqachilarni va ular bilan bog'liq albomlarni chiqaring.
select artist.name, album.title
from artist
inner join album
on album.ArtistId = artist.ArtistId;

# 2.	Chinook ma’lumotlar bazasidagi Customer va Invoice jadvallarini qo‘shib, har bir mijozning ismi,familyasi,invoice sanasi va to‘lov ma’lumotlarini chiqaring.
SELECT Customer.FirstName, Customer.LastName, Invoice.InvoiceDate, Invoice.Total
FROM Customer
INNER JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId;

# 3.	Chinook ma'lumotlar bazasidagi Track va Genre jadvallarini qo‘shib, har bir trekning nomi va janrini chiqaring.
SELECT Track.Name AS TrackName, Genre.Name AS GenreName
FROM Track
INNER JOIN Genre ON Track.GenreId = Genre.GenreId;

# 4.	Chinook ma'lumotlar bazasidagi InvoiceLine va Track jadvallarini qo‘shib, har bir invoice chizig‘idagi trek nomini va ularning narxini chiqaring.
SELECT InvoiceLine.InvoiceId, Track.Name AS TrackName, InvoiceLine.UnitPrice
FROM InvoiceLine
INNER JOIN Track ON InvoiceLine.TrackId = Track.TrackId;

# 5.	Chinook ma'lumotlar bazasidagi Album va Track jadvallarini qo‘shib, har bir albomdagi treklar ro‘yxatini chiqaring.
SELECT Album.Title AS AlbumTitle, Track.Name AS TrackName
FROM Album
INNER JOIN Track ON Album.AlbumId = Track.AlbumId;

# 6.	Chinook ma'lumotlar bazasidagi Employee va Customer jadvallarini qo‘shib, har bir mijoz va unga tayinlangan xodimning ismini chiqaring.
SELECT Customer.FirstName AS CustomerFirstName, Customer.LastName AS CustomerLastName,
       Employee.FirstName AS EmployeeFirstName, Employee.LastName AS EmployeeLastName
FROM Customer
INNER JOIN Employee ON Customer.SupportRepId = Employee.EmployeeId;

# 7.	Chinook ma'lumotlar bazasidagi PlaylistTrack va Track jadvallarini qo‘shib, har bir pleylistdagi treklar ro‘yxatini chiqaring.
SELECT Playlist.Name AS PlaylistName, Track.Name AS TrackName
FROM Playlist
INNER JOIN PlaylistTrack ON Playlist.PlaylistId = PlaylistTrack.PlaylistId
INNER JOIN Track ON PlaylistTrack.TrackId = Track.TrackId;

# 8.	Chinook ma'lumotlar bazasidagi MediaType va Track jadvallarini qo‘shib, har bir trekning nomi va uning media turini chiqaring.
SELECT Track.Name AS TrackName, MediaType.Name AS MediaTypeName
FROM Track
INNER JOIN MediaType ON Track.MediaTypeId = MediaType.MediaTypeId;

# 9.	Chinook ma'lumotlar bazasidagi Customer va Invoice jadvallarini qo‘shib, faqat 10 dollar yoki undan ortiq to‘lovni amalga oshirgan  mijozlarning ID raqamini,  ism va familyasini(bir ustunda, Fullname deb nomlang)  va to‘lov summalarini ko‘rsating.
SELECT Customer.CustomerId, 
       (Customer.FirstName || ' ' || Customer.LastName) AS FullName, 
       Invoice.Total
FROM Customer
INNER JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
WHERE Invoice.Total >= 10;

# 10.	Chinook ma'lumotlar bazasidan har bir qo'shiq (Track) va unga mos keladigan albom (Album) nomini toping.
SELECT Track.Name AS TrackName, Album.Title AS AlbumTitle
FROM Track
INNER JOIN Album ON Track.AlbumId = Album.AlbumId;
































