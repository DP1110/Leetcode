1class Solution:
2    def uniquePaths(self, m, n):
3        dp = [1] * n  # first row is all 1s
4        
5        for i in range(1, m):
6            for j in range(1, n):
7                dp[j] += dp[j - 1]
8        
9        return dp[-1]