class Solution:
    def isValid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:  # It's a closing bracket
                # Pop from stack if possible, else use dummy value
                top = stack.pop() if stack else '#'
                if top != mapping[char]:
                    return False
            else:  # It's an opening bracket
                stack.append(char)
        
        # Valid only if all brackets were matched
        return len(stack) == 0