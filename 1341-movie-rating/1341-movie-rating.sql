(select name as results
from MovieRating r
INNER JOIN Users u on u.user_id = r.user_id
group by r.user_id
order by count(*) desc, name
limit 1)

union all

(
select title from 
(select r.movie_id, rating
    from MovieRating r where substr(created_at, 6, 2) = '02' AND substr(created_at, 1, 4) = '2020') r
INNER JOIN Movies m on r.movie_id = m.movie_id
group by r.movie_id
order by avg(rating) desc, title
limit 1
)