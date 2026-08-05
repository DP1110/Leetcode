1class Solution:
2    def combinationSum2(self, candidates, target):
3        candidates.sort()
4        result = []
5        
6        def backtrack(start, current, current_sum):
7            if current_sum == target:
8                result.append(current[:])
9                return
10            
11            for i in range(start, len(candidates)):
12                # Pruning
13                if current_sum + candidates[i] > target:
14                    break
15                
16                # Skip duplicates at the same level
17                if i > start and candidates[i] == candidates[i - 1]:
18                    continue
19                
20                current.append(candidates[i])
21                # i + 1 because each number can be used only once
22                backtrack(i + 1, current, current_sum + candidates[i])
23                current.pop()
24        
25        backtrack(0, [], 0)
26        return result