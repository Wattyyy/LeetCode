# https://leetcode.com/problems/employees-earning-more-than-their-managers/

# Write your MySQL query statement below
select 
    a.Name as 'Employee'
from 
    Employee as a, Employee as b
where 
    a.ManagerId = b.Id and a.salary > b.salary;
    
    
