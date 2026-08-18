1class Solution(object):
2    def calculateMinimumHP(self, dungeon):
3        """
4        :type dungeon: List[List[int]]
5        :rtype: int
6        """
7        m = len(dungeon)
8        n = len(dungeon[0])
9
10        dp = [[0] * n for _ in range(m)]
11
12        for i in range(m - 1, -1, -1):
13            for j in range(n - 1, -1, -1):
14                if i == m - 1 and j == n - 1:
15                    need = 1 - dungeon[i][j]
16                elif i == m - 1:
17                    need = dp[i][j + 1] - dungeon[i][j]
18                elif j == n - 1:
19                    need = dp[i + 1][j] - dungeon[i][j]
20                else:
21                    need = min(dp[i][j + 1], dp[i + 1][j]) - dungeon[i][j]
22
23                dp[i][j] = max(1, need)
24
25        return dp[0][0]