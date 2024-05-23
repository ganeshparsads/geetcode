# Write your MySQL query statement below
# select query_name,
# # count(query_name)
# round(avg(rating / position), 2) as quality,
# round(sum(case when rating < 3 then 1 else 0 end) / count(query_name)*100, 2) as poor_query_percentage
# from queries
# where query_name is NOT null
# group by query_name;

SELECT q1.query_name, ROUND(SUM(q1.rating/q1.position)/S, 2) as quality, ROUND((SUM(CASE when q1.rating < 3 
then 1 ELSE 0 END)/S)*100, 2) as poor_query_percentage FROM Queries q1 JOIN (SELECT COUNT(*) as S, query_name FROM Queries GROUP BY query_name) as a
ON q1.query_name = a.query_name
GROUP BY q1.query_name