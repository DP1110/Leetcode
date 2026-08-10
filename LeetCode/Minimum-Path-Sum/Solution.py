1class Solution:
2    def minPathSum(self, grid):
3        m = len(grid)
4        n = len(grid[0])
5        
6        dp = [0] * n
7        dp[0] = grid[0][0]
8        
9        for j in range(1, n):
10            dp[j] = dp[j - 1] + grid[0][j]
11        
12        for i in range(1, m):
13            dp[0] += grid[i][0]
14            for j in range(1, n):
15                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
16        
17        return dp[-1]