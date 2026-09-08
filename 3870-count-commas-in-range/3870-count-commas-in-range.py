class Solution(object):
    def countCommas(self, n):
        total = 0
        lo = 1
        d = 1
        while lo <= n:
            hi = min(n, lo * 10 - 1)
            commas = (d - 1) // 3
            count = hi - lo + 1
            total += commas * count
            lo *= 10
            d += 1
        return total