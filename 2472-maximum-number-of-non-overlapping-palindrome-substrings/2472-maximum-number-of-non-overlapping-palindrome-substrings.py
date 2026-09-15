class Solution(object):
    def maxPalindromes(self, s, k):
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or is_pal[i+1][j-1]):
                    is_pal[i][j] = True

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i-1]
            for start in range(i - k, -1, -1):
                if is_pal[start][i-1]:
                    dp[i] = max(dp[i], dp[start] + 1)
                    break
        return dp[n]