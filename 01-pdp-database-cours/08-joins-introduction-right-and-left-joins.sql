# INNER JOIN 


# 1. Chinook ma'lumotlar bazasidagi Invoice, Customer, va Employee jadvallaridan har bir invoice uchun mijoz ismi va unga xizmat ko'rsatuvchi xodimning ismini ko'rsating.
SELECT Invoice.InvoiceId, Customer.FirstName || ' ' || Customer.LastName AS CustomerName,
       Employee.FirstName || ' ' || Employee.LastName AS EmployeeName
FROM Invoice
INNER JOIN Customer ON Invoice.CustomerId = Customer.CustomerId
INNER JOIN Employee ON Customer.SupportRepId = Employee.EmployeeId;

# 2. Chinook ma'lumotlar bazasidagi Track, Album, va Artist jadvallaridan har bir trek nomini, uning albomini va albom ijrochisini toping.
SELECT Track.Name AS TrackName, Album.Title AS AlbumTitle, Artist.Name AS ArtistName
FROM Track
INNER JOIN Album ON Track.AlbumId = Album.AlbumId
INNER JOIN Artist ON Album.ArtistId = Artist.ArtistId;

# 3. Chinook ma'lumotlar bazasidagi Track, Album, va Genre jadvallaridan har bir albom uchun janr bo'yicha treklarni ko'rsating.
SELECT Album.Title AS AlbumTitle, Genre.Name AS GenreName, Track.Name AS TrackName
FROM Track
INNER JOIN Album ON Track.AlbumId = Album.AlbumId
INNER JOIN Genre ON Track.GenreId = Genre.GenreId
ORDER BY Album.Title, Genre.Name;

# 4. Chinook ma'lumotlar bazasidagi Track, PlaylistTrack, va Playlist jadvallaridan har bir trek va uning qaysi pleylisitga tegishli ekanini toping.
SELECT Track.Name AS TrackName, Playlist.Name AS PlaylistName
FROM Track
INNER JOIN PlaylistTrack ON Track.TrackId = PlaylistTrack.TrackId
INNER JOIN Playlist ON PlaylistTrack.PlaylistId = Playlist.PlaylistId;

# 5. Chinook ma'lumotlar bazasidagi Track, MediaType, va Genre jadvallaridan har bir janr va media turining nomini ko'rsating.
SELECT Genre.Name AS GenreName, MediaType.Name AS MediaTypeName
FROM Track
INNER JOIN Genre ON Track.GenreId = Genre.GenreId
INNER JOIN MediaType ON Track.MediaTypeId = MediaType.MediaTypeId
GROUP BY GenreName, MediaTypeName
ORDER BY GenreName, MediaTypeName;

# 6. Chinook ma'lumotlar bazasidagi PlaylistTrack, Track, va MediaType jadvallaridan har bir pleylisitdagi treklar va ularning media turini ko'rsating.
SELECT Playlist.Name AS PlaylistName, Track.Name AS TrackName, MediaType.Name AS MediaTypeName
FROM Playlist
INNER JOIN PlaylistTrack ON Playlist.PlaylistId = PlaylistTrack.PlaylistId
INNER JOIN Track ON PlaylistTrack.TrackId = Track.TrackId
INNER JOIN MediaType ON Track.MediaTypeId = MediaType.MediaTypeId;

# 7. Chinook ma'lumotlar bazasidagi InvoiceLine, Track, Album, va Artist jadvallaridan har bir trekning albomi va uning ijrochisini ko'rsating.
SELECT InvoiceLine.InvoiceLineId, Track.Name AS TrackName, Album.Title AS AlbumTitle, Artist.Name AS ArtistName
FROM InvoiceLine
INNER JOIN Track ON InvoiceLine.TrackId = Track.TrackId
INNER JOIN Album ON Track.AlbumId = Album.AlbumId
INNER JOIN Artist ON Album.ArtistId = Artist.ArtistId;

# 8. Chinook ma'lumotlar bazasidagi Invoice, Customer jadvallari orqali har bir davlat bo'yicha umumiy invoice summasini hisoblang.
SELECT Customer.Country, SUM(Invoice.Total) AS TotalSales
FROM Invoice
INNER JOIN Customer ON Invoice.CustomerId = Customer.CustomerId
GROUP BY Customer.Country
ORDER BY TotalSales DESC;

# 9. Chinook ma'lumotlar bazasidagi InvoiceLine, Track, va Genre jadvallaridan har bir janr bo'yicha sotilgan treklar sonini hisoblang.
SELECT Genre.Name AS GenreName, COUNT(InvoiceLine.InvoiceLineId) AS NumberOfTracksSold
FROM InvoiceLine
INNER JOIN Track ON InvoiceLine.TrackId = Track.TrackId
INNER JOIN Genre ON Track.GenreId = Genre.GenreId
GROUP BY Genre.Name
ORDER BY NumberOfTracksSold DESC;

# 10. Chinook ma'lumotlar bazasi asosida, har bir janr bo'yicha qo'shiqlar sonini va ularning umumiy vaqtini hisoblang.
SELECT Genre.Name AS GenreName, COUNT(Track.TrackId) AS NumberOfTracks, 
       SUM(Track.Milliseconds / 1000) AS TotalDurationInSeconds
FROM Track
INNER JOIN Genre ON Track.GenreId = Genre.GenreId
GROUP BY Genre.Name
ORDER BY NumberOfTracks DESC;
