select distinct city from station
where not(city  like 'A%'
or city like 'E%'
or city like 'I%'
or city like 'O%'
or city like 'U%');
