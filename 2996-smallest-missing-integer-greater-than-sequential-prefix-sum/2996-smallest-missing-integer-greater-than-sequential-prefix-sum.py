class Solution:
    def missingInteger(self, nums):
        n = len(nums)
        
        # Find the longest sequential prefix
        prefix_end = 0
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                prefix_end = i
            else:
                break
        
        # Sum of the longest sequential prefix
        prefix_sum = sum(nums[:prefix_end + 1])
        
        # Find smallest missing integer >= prefix_sum
        seen = set(nums)
        x = prefix_sum
        while x in seen:
            x += 1
        
        return x