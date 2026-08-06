1class Solution:
2    def permuteUnique(self, nums):
3        nums.sort()
4        result = []
5        visited = [False] * len(nums)
6        
7        def backtrack(current):
8            if len(current) == len(nums):
9                result.append(current[:])
10                return
11            
12            for i in range(len(nums)):
13                if visited[i]:
14                    continue
15                
16                # Skip duplicates: only use nums[i] if nums[i-1] was used
17                # or if it's the first occurrence
18                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
19                    continue
20                
21                visited[i] = True
22                current.append(nums[i])
23                backtrack(current)
24                current.pop()
25                visited[i] = False
26        
27        backtrack([])
28        return result