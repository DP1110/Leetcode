class Solution(object):
    def numTrees(self, n):
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty tree
        
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        
        return dp[n]