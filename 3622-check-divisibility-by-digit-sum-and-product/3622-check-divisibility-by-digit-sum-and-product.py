class Solution(object):
    def checkDivisibility(self, n):
        s, p = 0, 1
        for d in str(n):
            d = int(d)
            s += d
            p *= d
        return n % (s + p) == 0