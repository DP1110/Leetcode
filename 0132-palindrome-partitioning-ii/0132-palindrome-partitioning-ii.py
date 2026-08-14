class Solution(object):
    def minCut(self, s):
        n = len(s)
        # is_pal[i][j] = True if s[i:j+1] is palindrome
        is_pal = [[False] * n for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True
        
        # dp[i] = min cuts for s[0:i+1]
        dp = [float('inf')] * n
        for i in range(n):
            if is_pal[0][i]:
                dp[i] = 0
            else:
                for j in range(i):
                    if is_pal[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)
        
        return dp[n - 1]