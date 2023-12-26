# Write your MySQL query statement below
SELECT 
    person_name
FROM (
    SELECT person_name, SUM(Weight)
    OVER(ORDER BY turn) AS Total_Weight
    FROM Queue
) AS P
WHERE Total_Weight<=1000
ORDER BY Total_Weight DESC LIMIT 1;
