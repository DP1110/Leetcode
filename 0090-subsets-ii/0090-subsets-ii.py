class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        result = []
        
        def backtrack(start, path):
            result.append(path[:])  # Add copy of current subset
            
            for i in range(start, len(nums)):
                # Skip duplicates at the same level
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(0, [])
        return result