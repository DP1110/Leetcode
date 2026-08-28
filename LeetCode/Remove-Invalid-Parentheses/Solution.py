1class Solution(object):
2    def removeInvalidParentheses(self, s):
3        def is_valid(st):
4            bal = 0
5            for c in st:
6                if c == '(':
7                    bal += 1
8                elif c == ')':
9                    bal -= 1
10                    if bal < 0:
11                        return False
12            return bal == 0
13
14        level = {s}
15        while True:
16            valid = [x for x in level if is_valid(x)]
17            if valid:
18                return valid
19            nxt = set()
20            for x in level:
21                for i in range(len(x)):
22                    if x[i] in '()':
23                        nxt.add(x[:i] + x[i+1:])
24            level = nxt