class Solution(object):
    def isInterleave(self, s1, s2, s3):
        m, n = len(s1), len(s2)
        
        # Quick length check
        if m + n != len(s3):
            return False
        
        # dp[i][j]: can s3[0:i+j] be formed by s1[0:i] and s2[0:j]?
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        
        # Fill first row: only s2 contributes
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        
        # Fill first column: only s1 contributes
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        
        # Fill rest
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                           (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        
        return dp[m][n]