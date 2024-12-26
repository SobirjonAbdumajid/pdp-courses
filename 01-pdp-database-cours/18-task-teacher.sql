SELECT * FROM customer.customer_sweepstakes;
alter table customer_sweepstakes rename column ï»¿sweepstake_id to sweepstake_id;

SELECT avg(income) FROM customer.customer_sweepstakes;

update customer_sweepstakes
 set phone=null
 where phone='';

 update customer_sweepstakes
 set income=null
 where income='';
 
 SELECT address, substring_index(address,',',1),
 substring_index(substring_index(address,',',2),',',-1),
 substring_index(address,',',-1)
 FROM customer_sweepstakes;
 
 alter table customer_sweepstakes add column street varchar(50) after address;
 alter table customer_sweepstakes add column city varchar(50) after street;
 alter table customer_sweepstakes add column state varchar(50) after city;
 
 update customer_sweepstakes
 set street=substring_index(address,',',1);
 
 update customer_sweepstakes
 set city=substring_index(substring_index(address,',',2),',',-1);
 
 update customer_sweepstakes
 set state=substring_index(address,',',-1);
 
 alter table customer_sweepstakes drop column address;
 
 
 SELECT favorite_color, trim(favorite_color) FROM customer.customer_sweepstakes;
 
  update customer_sweepstakes
 set favorite_color=trim(favorite_color);
 
 start transaction;
 update customer_sweepstakes
 set state=trim(favorite_color);
 rollback;