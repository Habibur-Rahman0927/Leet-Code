# Write your MySQL query statement below
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE pid IN (
    SELECT pid
    FROM Insurance
    GROUP BY lat * 1000 + lon
    HAVING COUNT(lat * 1000 + lon) = 1
    ) AND 
    tiv_2015 IN (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(tiv_2015) > 1
    )
