// https://leetcode.com/problems/classes-more-than-5-students

# Write your MySQL query statement below
select cnt_table.class 
from (
    select class, count(distinct student) as cnt
    from courses
    group by class
)
as cnt_table
where 5 <= cnt_table.cnt;
