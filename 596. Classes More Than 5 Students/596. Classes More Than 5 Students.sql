select `class` 
from (select `class`, count(distinct `student`) as `num`
     from `courses`
     group by `class`) as `tmp_table` 
where `num` >= 5;