# Write your MySQL query statement below
select customer_number from orders 
group by 1
order by count(distinct order_number) desc limit 1;