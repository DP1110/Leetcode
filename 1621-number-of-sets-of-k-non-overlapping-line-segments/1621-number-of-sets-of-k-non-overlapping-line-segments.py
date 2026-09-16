class Solution(object):
    def numberOfSets(self, n, k):
        MOD = 10 ** 9 + 7
        # dp[i][j][0] = ways using first i points, j segments, point i not covered by ongoing segment end
        # dp[i][j][1] = ways using first i points, j segments, point i IS the current open segment's right end (can extend)
        dp0 = [[0] * (k + 1) for _ in range(n)]
        dp1 = [[0] * (k + 1) for _ in range(n)]
        dp0[0][0] = 1
        for i in range(1, n):
            for j in range(k + 1):
                dp0[i][j] = (dp0[i-1][j] + dp1[i-1][j]) % MOD
                dp1[i][j] = dp1[i-1][j]
                if j > 0:
                    dp1[i][j] = (dp1[i][j] + dp0[i-1][j-1] + dp1[i-1][j-1]) % MOD
        return (dp0[n-1][k] + dp1[n-1][k]) % MOD