class Solution(object):
    def isScramble(self, s1, s2):
        memo = {}
        
        def dfs(s1, s2):
            if (s1, s2) in memo:
                return memo[(s1, s2)]
            
            # Direct match
            if s1 == s2:
                memo[(s1, s2)] = True
                return True
            
            # Pruning: character counts must match
            if sorted(s1) != sorted(s2):
                memo[(s1, s2)] = False
                return False
            
            n = len(s1)
            # Try every possible split point
            for i in range(1, n):
                # Case 1: No swap
                if dfs(s1[:i], s2[:i]) and dfs(s1[i:], s2[i:]):
                    memo[(s1, s2)] = True
                    return True
                
                # Case 2: Swap
                if dfs(s1[:i], s2[n-i:]) and dfs(s1[i:], s2[:n-i]):
                    memo[(s1, s2)] = True
                    return True
            
            memo[(s1, s2)] = False
            return False
        
        return dfs(s1, s2)