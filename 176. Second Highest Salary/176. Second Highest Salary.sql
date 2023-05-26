# Write your MySQL query statement below
select (select distinct(Salary) from Employee # Select only distinct Salary from the Employee table
order by Salary desc  # Order the Salary in descending order.
limit 1 offset 1) as SecondHighestSalary  # Taking the result from 2nd highest, limiting only 1 value