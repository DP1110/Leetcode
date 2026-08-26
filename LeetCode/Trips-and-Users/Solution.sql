1# Write your MySQL query statement below
2SELECT
3    t.request_at AS Day,
4    ROUND(
5        SUM(CASE WHEN t.status != 'completed' THEN 1 ELSE 0 END) / COUNT(*),
6        2
7    ) AS `Cancellation Rate`
8FROM Trips t
9JOIN Users cu ON t.client_id = cu.users_id AND cu.banned = 'No'
10JOIN Users du ON t.driver_id = du.users_id AND du.banned = 'No'
11WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
12GROUP BY t.request_at;