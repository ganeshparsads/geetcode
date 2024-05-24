# Write your MySQL query statement below

with cte as (
    select pid, tiv_2015, tiv_2016, CONCAT(lat, "-", lon) as latlon
    from Insurance
)

select round(sum(tiv_2016), 2) tiv_2016
from cte
where latlon not in (select latlon from cte group by latlon having count(*) > 1)
AND tiv_2015 in (select tiv_2015 from Insurance group by tiv_2015 having count(*) > 1 )

# select pid from Insurance group by tiv_2015 having count(*) > 1