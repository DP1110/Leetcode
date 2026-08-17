1class Solution(object):
2    def evalRPN(self, tokens):
3        """
4        :type tokens: List[str]
5        :rtype: int
6        """
7        stack = []
8        ops = set(['+', '-', '*', '/'])
9
10        for tok in tokens:
11            if tok in ops:
12                b = stack.pop()
13                a = stack.pop()
14                if tok == '+':
15                    res = a + b
16                elif tok == '-':
17                    res = a - b
18                elif tok == '*':
19                    res = a * b
20                else:
21                    # truncate toward zero, not floor
22                    res = int(a * 1.0 / b) if (a < 0) != (b < 0) else a // b
23                stack.append(res)
24            else:
25                stack.append(int(tok))
26
27        return stack.pop()