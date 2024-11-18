select * from artist;


# 1.	Chinook ma’lumotlar bazasidan Artist  jadvalidagi barcha musiqachilarni va ular bilan bog'liq albomlarni chiqaring.

select artist.name, album.title
from artist
inner join album
on album.ArtistId = artist.ArtistId;

































