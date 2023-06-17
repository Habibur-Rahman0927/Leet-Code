# Write your MySQL query statement below
select s1.Score, 
       (select count(distinct Score) 
                from Scores s2 WHERE s2.Score >= s1.Score)as 'Rank'
from Scores s1
order by s1.Score desc