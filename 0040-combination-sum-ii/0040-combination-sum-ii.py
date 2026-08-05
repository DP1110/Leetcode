class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        
        def backtrack(start, current, current_sum):
            if current_sum == target:
                result.append(current[:])
                return
            
            for i in range(start, len(candidates)):
                # Pruning
                if current_sum + candidates[i] > target:
                    break
                
                # Skip duplicates at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                current.append(candidates[i])
                # i + 1 because each number can be used only once
                backtrack(i + 1, current, current_sum + candidates[i])
                current.pop()
        
        backtrack(0, [], 0)
        return result