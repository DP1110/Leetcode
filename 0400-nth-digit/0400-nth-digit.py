class Solution(object):
    def findNthDigit(self, n):
        d = 1
        count = 9
        start = 1
        while n > d * count:
            n -= d * count
            d += 1
            count *= 10
            start *= 10
        num = start + (n - 1) // d
        idx = (n - 1) % d
        return int(str(num)[idx])