# Write your MySQL query statement below
SELECT *
FROM users
WHERE mail REGEXP '^[a-zA-Z][a-zAZ0-9_.-]*@leetcode[.]com'