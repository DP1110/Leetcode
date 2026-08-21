1# Write your MySQL query statement below
2SELECT w1.id
3FROM Weather w1
4JOIN Weather w2
5ON w1.recordDate = w2.recordDate + INTERVAL 1 DAY
6WHERE w1.temperature > w2.temperature;