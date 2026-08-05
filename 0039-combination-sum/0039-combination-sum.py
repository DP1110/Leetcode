class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        result = []
        
        def backtrack(start, current, current_sum):
            if current_sum == target:
                result.append(current[:])
                return
            
            for i in range(start, len(candidates)):
                # Pruning: since sorted, no need to check further
                if current_sum + candidates[i] > target:
                    break
                
                current.append(candidates[i])
                # Use i (not i+1) because we can reuse the same number
                backtrack(i, current, current_sum + candidates[i])
                current.pop()
        
        backtrack(0, [], 0)
        return result