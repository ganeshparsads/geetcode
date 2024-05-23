# Write your MySQL query statement below

select Prices.product_id, COALESCE(ROUND(sum(price * units) / sum(units), 2), 0) AS "average_price"
from Prices LEFT JOIN UnitsSold ON UnitsSold.product_id = Prices.product_id
AND UnitsSold.purchase_date BETWEEN Prices.start_date AND Prices.end_date
GROUP BY Prices.Product_id;