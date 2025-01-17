CREATE OR REPLACE FUNCTION loop_counter()
RETURNS void AS $$
DECLARE
    counter INT := 0;
BEGIN
    LOOP
        counter := counter + 1;
        RAISE NOTICE 'value: %', counter;
        IF counter > 5 THEN
            EXIT;
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION loop_counter()
RETURNS void AS $$
DECLARE
    counter INT := 0;
BEGIN
    while counter <= 5 LOOP
        counter := counter + 1; 
        RAISE NOTICE 'value: %', counter;
    END LOOP;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION loop_counter()
RETURNS void AS $$
DECLARE
    counter INT := 0;
BEGIN
    for i in 1..5 LOOP
        RAISE NOTICE 'value: %', i;
    END LOOP;
END;
$$ LANGUAGE plpgsql;


SELECT loop_counter();

-- ------------------------------------------------- --


CREATE TABLE IF NOT EXISTS my_table (
    id SERIAL PRIMARY KEY,
    uuid UUID DEFAULT gen_random_uuid()
);



CREATE OR REPLACE FUNCTION insert_random_uuids()
RETURNS void AS $$
DECLARE
    start_from INT := 0;
	num_rows INT=100;
BEGIN
    for i in start_from..num_rows LOOP
        INSERT INTO my_table (uuid) VALUES (gen_random_uuid());        
    END LOOP;
    
    RAISE NOTICE 'done';
END;
$$ LANGUAGE plpgsql;

select insert_random_uuids();

select * from my_table;
