class Solution(object):
    def minOperations(self, nums, x):
        total = sum(nums)
        target = total - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        n = len(nums)
        best = -1
        l = 0
        s = 0
        for r in range(n):
            s += nums[r]
            while s > target:
                s -= nums[l]
                l += 1
            if s == target:
                best = max(best, r - l + 1)

        return n - best if best != -1 else -1