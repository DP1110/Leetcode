1class Solution(object):
2    def isUgly(self, n):
3        if n <= 0:
4            return False
5        for p in (2, 3, 5):
6            while n % p == 0:
7                n //= p
8        return n == 1