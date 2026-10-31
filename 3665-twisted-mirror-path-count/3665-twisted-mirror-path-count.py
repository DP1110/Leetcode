class Solution:
    def uniquePaths(self, grid):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        A = [[0] * (n + 1) for _ in range(m + 1)]
        B = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                a, b = A[i][j], B[i][j]
                if grid[i][j] == 0:
                    t = a + b
                    if i == 0 and j == 0:
                        t = 1
                    t %= MOD
                    if i == m - 1 and j == n - 1:
                        return t
                    A[i][j + 1] = (A[i][j + 1] + t) % MOD
                    B[i + 1][j] = (B[i + 1][j] + t) % MOD
                else:
                    B[i + 1][j] = (B[i + 1][j] + a) % MOD
                    A[i][j + 1] = (A[i][j + 1] + b) % MOD
        return 0