class Solution(object):
    def countCommas(self, n):
        total = 0
        for x in range(1, n + 1):
            d = len(str(x))
            total += (d - 1) // 3
        return total