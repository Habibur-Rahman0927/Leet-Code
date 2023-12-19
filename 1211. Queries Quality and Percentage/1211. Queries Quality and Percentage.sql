# Write your MySQL query statement below
SELECT query_name, ROUND(AVG(rating / position), 2) AS quality, 
ROUND(AVG(IF(RATING < 3, 1, 0)) * 100, 2) AS poor_query_percentage
FROM queries
WHERE query_name IS NOT NULL
GROUP BY query_name;