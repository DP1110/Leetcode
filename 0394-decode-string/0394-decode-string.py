class Solution(object):
    def decodeString(self, s):
        stack = [["", 1]]
        num = ""
        for c in s:
            if c.isdigit():
                num += c
            elif c == '[':
                stack.append(["", int(num)])
                num = ""
            elif c == ']':
                st, k = stack.pop()
                stack[-1][0] += st * k
            else:
                stack[-1][0] += c
        return stack[0][0]