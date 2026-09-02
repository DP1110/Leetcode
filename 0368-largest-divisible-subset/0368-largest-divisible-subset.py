class Solution(object):
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        dp = [1] * n
        parent = [-1] * n

        best_idx = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j
            if dp[i] > dp[best_idx]:
                best_idx = i

        res = []
        i = best_idx
        while i != -1:
            res.append(nums[i])
            i = parent[i]
        return res[::-1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna