# Write your MySQL query statement below
select e.name, euni.unique_id
from Employees e
Left Join EmployeeUNI euni
ON e.id = euni.id;
