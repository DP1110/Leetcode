1class Solution:
2    def maxSubArray(self, nums):
3        cur = best = nums[0]
4        for x in nums[1:]:
5            cur = max(x, cur + x)
6            best = max(best, cur)
7        return best