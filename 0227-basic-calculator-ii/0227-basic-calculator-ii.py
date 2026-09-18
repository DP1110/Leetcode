class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        op = '+'
        n = len(s)
        for i in xrange(n):
            c = s[i]
            if c.isdigit():
                num = num*10 + int(c)
            if (not c.isdigit() and c != ' ') or i == n-1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop()*num)
                elif op == '/':
                    prev = stack.pop()
                    q = abs(prev)//abs(num)
                    if (prev < 0) != (num < 0):
                        q = -q
                    stack.append(q)
                op = c
                num = 0
        return sum(stack)