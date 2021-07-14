// https://leetcode.com/problems/customers-who-never-order

# Write your MySQL query statement below
select
    tmp.Name as Customers
from (
    select 
        Customers.Id, Customers.Name, Orders.CustomerId
    from Customers
    left join Orders on Customers.Id = Orders.CustomerId
    )
as tmp
where
    tmp.CustomerId is null;
    