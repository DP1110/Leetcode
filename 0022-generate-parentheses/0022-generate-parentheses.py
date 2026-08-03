class Solution:
    def generateParenthesis(self, n):
        result = []
        
        def backtrack(current, open_count, close_count):
            # Base case: used all n pairs
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # Can add '(' if we haven't used all n
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
            
            # Can add ')' if it won't exceed '(' count
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)
        
        backtrack("", 0, 0)
        return result