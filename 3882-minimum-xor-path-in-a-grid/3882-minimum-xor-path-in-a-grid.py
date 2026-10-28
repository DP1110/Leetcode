class Solution:
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        prev = [set() for _ in range(n)]

        for i in range(m):
            cur = [set() for _ in range(n)]
            for j in range(n):
                g = grid[i][j]
                if i == 0 and j == 0:
                    cur[j] = {g}
                    continue
                src = set()
                if i > 0:
                    src |= prev[j]
                if j > 0:
                    src |= cur[j - 1]
                cur[j] = {v ^ g for v in src}
            prev = cur

        return min(prev[n - 1])