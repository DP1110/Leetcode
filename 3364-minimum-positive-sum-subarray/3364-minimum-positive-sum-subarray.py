class Solution:
    def minimumSumSubarray(self, nums, l, r):
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]
        best = -1
        for length in range(l, r + 1):
            for i in range(n - length + 1):
                s = pre[i + length] - pre[i]
                if s > 0 and (best == -1 or s < best):
                    best = s
        return best