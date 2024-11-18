select * from artist;


# 1.	Chinook ma’lumotlar bazasidan Artist  jadvalidagi barcha musiqachilarni va ular bilan bog'liq albomlarni chiqaring.
select artist.name, album.title
from artist
inner join album
on album.ArtistId = artist.ArtistId;

# 2.	Chinook ma’lumotlar bazasidagi Customer va Invoice jadvallarini qo‘shib, har bir mijozning ismi,familyasi,invoice sanasi va to‘lov ma’lumotlarini chiqaring.


# 3.	Chinook ma'lumotlar bazasidagi Track va Genre jadvallarini qo‘shib, har bir trekning nomi va janrini chiqaring.


# 4.	Chinook ma'lumotlar bazasidagi InvoiceLine va Track jadvallarini qo‘shib, har bir invoice chizig‘idagi trek nomini va ularning narxini chiqaring.


# 5.	Chinook ma'lumotlar bazasidagi Album va Track jadvallarini qo‘shib, har bir albomdagi treklar ro‘yxatini chiqaring.


# 6.	Chinook ma'lumotlar bazasidagi Employee va Customer jadvallarini qo‘shib, har bir mijoz va unga tayinlangan xodimning ismini chiqaring.


# 7.	Chinook ma'lumotlar bazasidagi PlaylistTrack va Track jadvallarini qo‘shib, har bir pleylistdagi treklar ro‘yxatini chiqaring.


# 8.	Chinook ma'lumotlar bazasidagi MediaType va Track jadvallarini qo‘shib, har bir trekning nomi va uning media turini chiqaring.


# 9.	Chinook ma'lumotlar bazasidagi Customer va Invoice jadvallarini qo‘shib, faqat 10 dollar yoki undan ortiq to‘lovni amalga oshirgan  mijozlarning ID raqamini,  ism va familyasini(bir ustunda, Fullname deb nomlang)  va to‘lov summalarini ko‘rsating.


# 10.	Chinook ma'lumotlar bazasidan har bir qo'shiq (Track) va unga mos keladigan albom (Album) nomini toping.
































