class Solution:
    def findMissingElements(self, nums):
        min_val = min(nums)
        max_val = max(nums)
        num_set = set(nums)
        
        missing = []
        for num in range(min_val, max_val + 1):
            if num not in num_set:
                missing.append(num)
        
        return missing