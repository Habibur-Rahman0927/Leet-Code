# Write your MySQL query statement below
SELECT Name AS Customers
FROM Customers 
LEFT JOIN Orders
ON Customers.Id = Orders.CustomerId
WHERE Orders.CustomerId is NULL

select c.Name as Customers
from Customers c
where c.Id not in (select CustomerId from Orders)