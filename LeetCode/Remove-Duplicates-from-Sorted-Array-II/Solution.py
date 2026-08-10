1class Solution(object):
2    def removeDuplicates(self, nums):
3        k = 0
4        for num in nums:
5            if k < 2 or num != nums[k - 2]:
6                nums[k] = num
7                k += 1
8        return k