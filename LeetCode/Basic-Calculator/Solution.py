1class Solution(object):
2    def calculate(self, s):
3        result = 0
4        num = 0
5        sign = 1
6        stack = []
7
8        for ch in s:
9            if ch.isdigit():
10                num = num * 10 + int(ch)
11            elif ch in '+-':
12                result += sign * num
13                num = 0
14                sign = 1 if ch == '+' else -1
15            elif ch == '(':
16                stack.append(result)
17                stack.append(sign)
18                result = 0
19                sign = 1
20            elif ch == ')':
21                result += sign * num
22                num = 0
23                result *= stack.pop()
24                result += stack.pop()
25
26        result += sign * num
27        return result