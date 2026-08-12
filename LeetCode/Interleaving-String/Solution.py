1class Solution(object):
2    def isInterleave(self, s1, s2, s3):
3        m, n = len(s1), len(s2)
4        
5        # Quick length check
6        if m + n != len(s3):
7            return False
8        
9        # dp[i][j]: can s3[0:i+j] be formed by s1[0:i] and s2[0:j]?
10        dp = [[False] * (n + 1) for _ in range(m + 1)]
11        dp[0][0] = True
12        
13        # Fill first row: only s2 contributes
14        for j in range(1, n + 1):
15            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
16        
17        # Fill first column: only s1 contributes
18        for i in range(1, m + 1):
19            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
20        
21        # Fill rest
22        for i in range(1, m + 1):
23            for j in range(1, n + 1):
24                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
25                           (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
26        
27        return dp[m][n]