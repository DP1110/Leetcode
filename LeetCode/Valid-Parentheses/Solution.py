1class Solution:
2    def isValid(self, s):
3        stack = []
4        mapping = {')': '(', '}': '{', ']': '['}
5        
6        for char in s:
7            if char in mapping:  # It's a closing bracket
8                # Pop from stack if possible, else use dummy value
9                top = stack.pop() if stack else '#'
10                if top != mapping[char]:
11                    return False
12            else:  # It's an opening bracket
13                stack.append(char)
14        
15        # Valid only if all brackets were matched
16        return len(stack) == 0