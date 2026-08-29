1class Solution(object):
2    def maxCoins(self, nums):
3        balloons = [1] + nums + [1]
4        n = len(balloons)
5        dp = [[0] * n for _ in range(n)]
6
7        for length in range(2, n):
8            for left in range(0, n - length):
9                right = left + length
10                best = 0
11                for k in range(left + 1, right):
12                    val = dp[left][k] + dp[k][right] + balloons[left] * balloons[k] * balloons[right]
13                    if val > best:
14                        best = val
15                dp[left][right] = best
16        return dp[0][n - 1]