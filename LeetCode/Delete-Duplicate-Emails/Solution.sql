1# Write your MySQL query statement below
2DELETE p1 FROM Person p1
3JOIN Person p2
4ON p1.email = p2.email AND p1.id > p2.id;