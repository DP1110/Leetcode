1class Solution:
2    def longestValidParentheses(self, s):
3        stack = [-1]  # Base index for length calculation
4        max_len = 0
5        
6        for i, char in enumerate(s):
7            if char == '(':
8                stack.append(i)
9            else:
10                stack.pop()
11                if not stack:
12                    stack.append(i)  # New base for future matches
13                else:
14                    max_len = max(max_len, i - stack[-1])
15        
16        return max_len