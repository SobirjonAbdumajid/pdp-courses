start transaction;

select count(phone) from customer_sweepstakes;
select * from customer_sweepstakes;


update customer_sweepstakes 
set `Are you over 18?`=case
when `Are you over 18?`='Yes' then 'Y'
when `Are you over 18?`='No' then 'N'
else `Are you over 18?` end;

update customer_sweepstakes
set phone=regexp_replace(phone, '[()/<>=+-]', '');

update customer_sweepstakes
set phone=null
where phone = '';

update customer_sweepstakes
set income=null
where income='';

update customer_sweepstakes
set phone=concat(substring(phone, 1, 3), '-', substring(phone, 4, 3), '-', substring(phone, 7));

select address, substring_index2(address, ',', 1);


select favorite_color, trim(favorite_color) from customer_sweepstakes;

update customer_sweepstakes
set favorite_color=trim(favorite_color);

alter table

rollback;