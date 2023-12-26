# Write your MySQL query statement below
SELECT visits.visited_on AS visited_on,
    SUM(c.amount) AS amount,
    ROUND(SUM(c.amount) / 7.0, 2) AS average_amount
FROM (
    SELECT DISTINCT visited_on
    FROM Customer
    WHERE DATEDIFF(
        visited_on,
        (SELECT MIN(visited_on) FROM Customer)
    ) >= 6
) visits
LEFT JOIN Customer c
ON DATEDIFF(visits.visited_on, c.visited_on) BETWEEN 0 AND 6
GROUP BY visits.visited_on
ORDER BY visited_on