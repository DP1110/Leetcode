class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # Quick check: if start or destination is blocked
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0
        
        # dp[j] = number of ways to reach column j in the current row
        dp = [0] * n
        dp[0] = 1  # Starting position
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0           # Obstacle: no ways to reach here
                elif j > 0:
                    dp[j] += dp[j - 1]  # From above (dp[j]) + from left (dp[j-1])
                # j == 0: dp[0] keeps value from cell above (previous row)
        
        return dp[-1]