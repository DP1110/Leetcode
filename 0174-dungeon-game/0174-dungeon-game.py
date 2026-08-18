class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])

        dp = [[0] * n for _ in range(m)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    need = 1 - dungeon[i][j]
                elif i == m - 1:
                    need = dp[i][j + 1] - dungeon[i][j]
                elif j == n - 1:
                    need = dp[i + 1][j] - dungeon[i][j]
                else:
                    need = min(dp[i][j + 1], dp[i + 1][j]) - dungeon[i][j]

                dp[i][j] = max(1, need)

        return dp[0][0]