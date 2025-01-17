create trigger after_user_update
after update on users
for each row
execute procedure log_in_audit();

create or replace function log_in_audit()
returns trigger
language plpgsql
as
$$
begin
	insert into audit_log (user_id, action, change_item)
	values (old.id, 'User updated', now());
	return new;
end
$$;


insert into users (first_name, last_name, age)
values ('Alex', 'Martinez', 15)

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT
);


CREATE TABLE audit_log (
    id SERIAL PRIMARY KEY,
    user_id INT,
    action VARCHAR(50),
    change_item TIMESTAMP
);


update users
set age = 20
where first_name='Alex';


drop table audit_log;


select * from users;