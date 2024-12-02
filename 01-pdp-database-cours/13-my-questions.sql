select * from artist;
select PlaylistId, Name as Name_of_my_playlist from playlist;
select * from playlisttrack;

# 1 - Har playlist necha marta ko'rildi (playlisttrack'da bor) bunda playlist name'ni va necha marta ko'rilganini chiqaring
select Playlist.name, count(playlisttrack.PlaylistId)
from playlisttrack
join playlist on playlisttrack.PlaylistId = playlist.PlaylistId
group by playlist.PlaylistId;

# 2 - Har bir Artistning nechta albomi bor bunda artistning nomi bilan soniga qarab tartib bilan guruhlang va umumiy soni ham bo'lsin.
select artist.Name, count(album.AlbumId)
from album
join artist on album.ArtistId = artist.ArtistId
group by artist.Name
with rollup
order by count(album.AlbumId);

# 3 - Har bir davlatning nechta shahari bor bunda nomi bilan soniga qarab tartib bilan guruhlang va umumiy soni ham bo'lsin
select * from country;
select * from city;
select country.country, count(city.city)
from country
join city on country.country_id= city.country_id
group by country.country
with rollup
order by count(city.city);

# 4 - Film'larni rantal_rate 4 dan balandlarini title bilan chiqaring
select title, rental_rate from film where rental_rate > 4 ;

# 5 - Har bir customer'ning nomi bilan addressini chiqaring
select customer.first_name, address.address
from customer
join address on customer.address_id = address.address_id;

# 6 - Staff'ning ismi bilan address'sining nomini chiqaring
select staff.first_name, address.address
from staff
join address on staff.address_id = address.address_id;
