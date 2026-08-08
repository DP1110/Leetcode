class Solution:
    def permute(self, nums):
        result = []
        
        def backtrack(current, visited):
            if len(current) == len(nums):
                result.append(current[:])
                return
            
            for num in nums:
                if num not in visited:
                    visited.add(num)
                    current.append(num)
                    backtrack(current, visited)
                    current.pop()
                    visited.remove(num)
        
        backtrack([], set())
        return result