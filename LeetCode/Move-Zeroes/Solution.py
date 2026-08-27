1class Solution(object):
2    def moveZeroes(self, nums):
3        pos = 0
4        for i in range(len(nums)):
5            if nums[i] != 0:
6                nums[pos], nums[i] = nums[i], nums[pos]
7                pos += 1