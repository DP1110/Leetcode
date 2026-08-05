class Solution:
    def longestValidParentheses(self, s):
        stack = [-1]  # Base index for length calculation
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)  # New base for future matches
                else:
                    max_len = max(max_len, i - stack[-1])
        
        return max_len