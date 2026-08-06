1class Solution:
2    def permute(self, nums):
3        result = []
4        n = len(nums)
5        
6        def backtrack(start):
7            if start == n:
8                result.append(nums[:])
9                return
10            
11            for i in range(start, n):
12                nums[start], nums[i] = nums[i], nums[start]
13                backtrack(start + 1)
14                nums[start], nums[i] = nums[i], nums[start]  # backtrack
15        
16        backtrack(0)
17        return result