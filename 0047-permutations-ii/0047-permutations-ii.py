class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        result = []
        visited = [False] * len(nums)
        
        def backtrack(current):
            if len(current) == len(nums):
                result.append(current[:])
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue
                
                # Skip duplicates: only use nums[i] if nums[i-1] was used
                # or if it's the first occurrence
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                
                visited[i] = True
                current.append(nums[i])
                backtrack(current)
                current.pop()
                visited[i] = False
        
        backtrack([])
        return result