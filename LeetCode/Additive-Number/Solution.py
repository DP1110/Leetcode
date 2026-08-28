1class Solution(object):
2    def isAdditiveNumber(self, num):
3        n = len(num)
4
5        def valid(s):
6            return s == "0" or s[0] != "0"
7
8        for i in range(1, n):
9            for j in range(i + 1, n):
10                a, b = num[:i], num[i:j]
11                if not valid(a) or not valid(b):
12                    continue
13                x, y = int(a), int(b)
14                pos = j
15                while pos < n:
16                    s = x + y
17                    s_str = str(s)
18                    if num[pos:pos+len(s_str)] != s_str:
19                        break
20                    pos += len(s_str)
21                    x, y = y, s
22                if pos == n:
23                    return True
24        return False