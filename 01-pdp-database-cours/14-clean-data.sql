

alter table cleandata rename column ﻿sweepstakes_id to ﻿sweepstake_id;

SELECT * FROM cleandata;

select phone, regexp_replace(phone, '[()/<>=+-]', '') from cleandata;

update cleandata
set phone=regexp_replace(phone, '[()/<>=+-]', '');

select phone, concat(substring(phone,1,3),'-',substring(phone, 4,3),'-', substring(phone,7)) from cleandata;

update cleandata
set phone=concat(substring(phone,1,3),'-',substring(phone, 4,3),'-', substring(phone,7));

