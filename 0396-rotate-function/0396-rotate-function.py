class Solution(object):
    def maxRotateFunction(self, nums):
        n = len(nums)
        total = sum(nums)
        f = sum(i * x for i, x in enumerate(nums))
        best = f
        for k in range(1, n):
            f += total - n * nums[n - k]
            best = max(best, f)
        return best