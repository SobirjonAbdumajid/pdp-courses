

alter table cleandata rename column ﻿sweepstakes_id to ﻿sweepstake_id;

SELECT * FROM cleandata;

select phone, regexp_replace(phone, '[()/<>=+-]', '') from cleandata;

update cleandata
set phone=regexp_replace(phone, '[()/<>=+-]', '');

select phone, concat(substring(phone,1,3),'-',substring(phone, 4,3),'-', substring(phone,7)) from cleandata;

update cleandata
set phone=concat(substring(phone,1,3),'-',substring(phone, 4,3),'-', substring(phone,7));

select favorite_color, upper(favorite_color) from cleandata;

update cleandata
set favorite_color=upper(favorite_color);

select `Are you over 18?`, case
when `Are you over 18?`='Yes' then 'Y'
when `Are you over 18?`='No' then 'N'
else `Are you over 18?` end from cleandata;

update cleandata
set `Are you over 18?`=case
when `Are you over 18?`='Yes' then 'Y'
when `Are you over 18?`='No' then 'N'
else `Are you over 18?` end;


