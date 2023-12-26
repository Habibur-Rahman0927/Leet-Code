# Write your MySQL query statement below
SELECT request_at AS Day, 
    ROUND(SUM(IF(status = 'completed', 0, 1)) / COUNT(status), 2) AS 'Cancellation Rate'
FROM Trips
WHERE client_id NOT IN (SELECT users_id FROM Users WHERE Banned = "Yes")
    AND driver_id NOT IN (SELECT users_id FROM Users WHERE Banned = "Yes")
    AND request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY request_at