1class Solution(object):
2    def calculate(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        stack = []
8        num = 0
9        op = '+'
10        n = len(s)
11        for i in xrange(n):
12            c = s[i]
13            if c.isdigit():
14                num = num*10 + int(c)
15            if (not c.isdigit() and c != ' ') or i == n-1:
16                if op == '+':
17                    stack.append(num)
18                elif op == '-':
19                    stack.append(-num)
20                elif op == '*':
21                    stack.append(stack.pop()*num)
22                elif op == '/':
23                    prev = stack.pop()
24                    q = abs(prev)//abs(num)
25                    if (prev < 0) != (num < 0):
26                        q = -q
27                    stack.append(q)
28                op = c
29                num = 0
30        return sum(stack)