class Solution:
    def removeDuplicates(self, nums):
        k = 0
        
        for num in nums:
            if k == 0 or num != nums[k - 1]:
                nums[k] = num
                k += 1
        
        return k