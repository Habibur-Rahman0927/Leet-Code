# Write your MySQL query statement below
SELECT s.user_id, round(avg(if(c.action='confirmed', 1, 0)), 2) confirmation_rate FROM Signups s 
LEFT JOIN Confirmations c ON c.user_id = s.user_id 
GROUP BY s.user_id;