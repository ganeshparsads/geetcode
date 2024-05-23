# Write your MySQL query statement below
WITH cte AS (
    SELECT product_id, min(year) first_year FROM Sales
    GROUP BY product_id
)

SELECT
    cte.product_id,
    first_year,
    quantity,
    price
FROM Sales JOIN cte ON Sales.product_id = cte.product_id 
                    AND Sales.year = cte.first_year
                    JOIN Product p on cte.product_id = p.product_id