class Solution(object):
    def getMoneyAmount(self, n):
        dp = [[0] * (n + 1) for _ in range(n + 2)]
        for lo in range(n, 0, -1):
            for hi in range(lo + 1, n + 1):
                best = float('inf')
                for x in range(lo, hi + 1):
                    left = dp[lo][x-1] if x - 1 >= lo else 0
                    right = dp[x+1][hi] if x + 1 <= hi else 0
                    cost = x + max(left, right)
                    best = min(best, cost)
                dp[lo][hi] = best
        return dp[1][n]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna