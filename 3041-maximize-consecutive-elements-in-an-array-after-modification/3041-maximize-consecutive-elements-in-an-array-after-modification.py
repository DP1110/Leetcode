class Solution:
    def maxSelectedElements(self, nums):
        nums.sort()
        dp = {}
        best = 1
        for x in nums:
            a = dp.get(x, 0) + 1
            b = dp.get(x - 1, 0) + 1
            dp[x + 1] = a
            dp[x] = b
            if a > best:
                best = a
            if b > best:
                best = b
        return best