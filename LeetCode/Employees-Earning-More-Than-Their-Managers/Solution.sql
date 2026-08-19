1SELECT e1.name AS Employee
2FROM Employee e1
3JOIN Employee e2 ON e1.managerId = e2.id
4WHERE e1.salary > e2.salary;