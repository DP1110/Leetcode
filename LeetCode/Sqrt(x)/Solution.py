1class Solution(object):
2    def mySqrt(self, x):
3        if x < 2:
4            return x
5        r = x
6        while r * r > x:
7            r = (r + x // r) // 2
8        return r