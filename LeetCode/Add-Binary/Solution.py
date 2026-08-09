1class Solution(object):
2    def addBinary(self, a, b):
3        i, j = len(a) - 1, len(b) - 1
4        carry = 0
5        res = []
6        
7        while i >= 0 or j >= 0 or carry:
8            total = carry
9            if i >= 0:
10                total += int(a[i])
11                i -= 1
12            if j >= 0:
13                total += int(b[j])
14                j -= 1
15            res.append(str(total % 2))
16            carry = total // 2
17        
18        return "".join(reversed(res))