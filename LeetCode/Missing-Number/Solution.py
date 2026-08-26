1class Solution(object):
2    def missingNumber(self, nums):
3        n = len(nums)
4        return n * (n + 1) // 2 - sum(nums)