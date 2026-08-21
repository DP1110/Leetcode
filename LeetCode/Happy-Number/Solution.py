1class Solution(object):
2    def isHappy(self, n):
3        seen = set()
4        while n != 1 and n not in seen:
5            seen.add(n)
6            n = sum(int(d) ** 2 for d in str(n))
7        return n == 1