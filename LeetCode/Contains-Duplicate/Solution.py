1class Solution(object):
2    def containsDuplicate(self, nums):
3        return len(nums) != len(set(nums))