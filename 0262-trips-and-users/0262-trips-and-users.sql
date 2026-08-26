# Write your MySQL query statement below
SELECT
    t.request_at AS Day,
    ROUND(
        SUM(CASE WHEN t.status != 'completed' THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS `Cancellation Rate`
FROM Trips t
JOIN Users cu ON t.client_id = cu.users_id AND cu.banned = 'No'
JOIN Users du ON t.driver_id = du.users_id AND du.banned = 'No'
WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY t.request_at;