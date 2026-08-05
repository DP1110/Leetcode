1class Solution:
2    def combinationSum(self, candidates, target):
3        candidates.sort()
4        result = []
5        
6        def backtrack(start, current, current_sum):
7            if current_sum == target:
8                result.append(current[:])
9                return
10            
11            for i in range(start, len(candidates)):
12                # Pruning: since sorted, no need to check further
13                if current_sum + candidates[i] > target:
14                    break
15                
16                current.append(candidates[i])
17                # Use i (not i+1) because we can reuse the same number
18                backtrack(i, current, current_sum + candidates[i])
19                current.pop()
20        
21        backtrack(0, [], 0)
22        return result