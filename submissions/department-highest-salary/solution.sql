// https://leetcode.com/problems/department-highest-salary

# Write your MySQL query statement below
select 
    Department.Name as Department, 
    Employee.Name as Employee,
    Employee.Salary
from 
    Employee, 
    (
    select DepartmentId, max(Salary) as MaxSalary
    from Employee
    group by DepartmentId
    ) as T
join 
    Department on DepartmentId = Department.Id
where 
    Employee.DepartmentId = T.DepartmentId and 
    Employee.Salary = T.MaxSalary;