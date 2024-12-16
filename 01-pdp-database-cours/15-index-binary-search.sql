create table stores (
	id serial primary key,
	name text,
	location POINT
);


create index location_gist_idx on stores using GIST(location);

insert into stores (name, location)
values
	('Store A', POINT(1, 1)),
	('Store B', POINT(2, 2)),
	('Store C', POINT(3, 3)),
	('Store D', POINT(6, 6)),
	('Store E', POINT(4, 4)),
	('Store F', POINT(0, 0)),
	('Store G', POINT(5, 5));

select name from stores where location <@ BOX '((0, 0), (6, 6))';