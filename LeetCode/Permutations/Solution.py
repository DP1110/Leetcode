1class Solution:
2    def permute(self, nums):
3        result = []
4        
5        def backtrack(current, visited):
6            if len(current) == len(nums):
7                result.append(current[:])
8                return
9            
10            for num in nums:
11                if num not in visited:
12                    visited.add(num)
13                    current.append(num)
14                    backtrack(current, visited)
15                    current.pop()
16                    visited.remove(num)
17        
18        backtrack([], set())
19        return result