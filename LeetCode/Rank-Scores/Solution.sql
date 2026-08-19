1SELECT
2    score,
3    DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
4FROM Scores
5ORDER BY score DESC;