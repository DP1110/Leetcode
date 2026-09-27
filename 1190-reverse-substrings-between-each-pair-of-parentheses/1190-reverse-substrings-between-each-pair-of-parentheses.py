class Solution(object):
    def reverseParentheses(self, s):
        stack = [[]]
        for c in s:
            if c == '(':
                stack.append([])
            elif c == ')':
                top = stack.pop()
                top.reverse()
                stack[-1].extend(top)
            else:
                stack[-1].append(c)
        return ''.join(stack[0])