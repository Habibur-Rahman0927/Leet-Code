# Write your MySQL query statement below
SELECT p.product_id, p.product_name FROM Product p 
LEFT JOIN Sales s ON s.product_id = p.product_id
GROUP BY s.product_id
HAVING MIN(s.sale_date) >= '2019-01-01' and MAX(s.sale_date) <= '2019-03-31';