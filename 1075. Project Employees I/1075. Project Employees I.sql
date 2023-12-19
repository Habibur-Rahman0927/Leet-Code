# Write your MySQL query statement below
SELECT P.project_id, ROUND(avg(E.experience_years), 2) AS average_years 
FROM Employee E
JOIN Project P ON E.employee_id = P.employee_id
GROUP BY P.project_id
ORDER BY P.project_id;