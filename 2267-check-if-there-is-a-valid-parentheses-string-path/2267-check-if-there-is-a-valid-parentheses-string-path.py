class Solution(object):
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        if (m + n - 1) % 2 != 0:
            return False
        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False

        # dp[j] = set of possible balance values at cell (i, j)
        dp = [set() for _ in range(n)]
        dp[0].add(1)
        for j in range(1, n):
            if not dp[j-1]:
                dp[j] = set()
                continue
            delta = 1 if grid[0][j] == '(' else -1
            dp[j] = {b + delta for b in dp[j-1] if b + delta >= 0}

        for i in range(1, m):
            new_dp = [set() for _ in range(n)]
            delta0 = 1 if grid[i][0] == '(' else -1
            new_dp[0] = {b + delta0 for b in dp[0] if b + delta0 >= 0}
            for j in range(1, n):
                delta = 1 if grid[i][j] == '(' else -1
                s = set()
                for b in dp[j]:
                    if b + delta >= 0:
                        s.add(b + delta)
                for b in new_dp[j-1]:
                    if b + delta >= 0:
                        s.add(b + delta)
                new_dp[j] = s
            dp = new_dp

        return 0 in dp[n-1]