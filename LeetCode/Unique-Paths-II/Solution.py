1class Solution:
2    def uniquePathsWithObstacles(self, obstacleGrid):
3        m = len(obstacleGrid)
4        n = len(obstacleGrid[0])
5        
6        # Quick check: if start or destination is blocked
7        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
8            return 0
9        
10        # dp[j] = number of ways to reach column j in the current row
11        dp = [0] * n
12        dp[0] = 1  # Starting position
13        
14        for i in range(m):
15            for j in range(n):
16                if obstacleGrid[i][j] == 1:
17                    dp[j] = 0           # Obstacle: no ways to reach here
18                elif j > 0:
19                    dp[j] += dp[j - 1]  # From above (dp[j]) + from left (dp[j-1])
20                # j == 0: dp[0] keeps value from cell above (previous row)
21        
22        return dp[-1]