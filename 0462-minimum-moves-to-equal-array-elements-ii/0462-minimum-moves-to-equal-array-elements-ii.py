class Solution:
    def minMoves2(self, nums):
        nums.sort()
        med = nums[len(nums) // 2]
        return sum(abs(x - med) for x in nums)