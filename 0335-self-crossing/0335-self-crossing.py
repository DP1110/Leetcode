class Solution(object):
    def isSelfCrossing(self, distance):
        d = distance
        n = len(d)
        for i in range(3, n):
            # case 1: current crosses line i-3
            if d[i] >= d[i-2] and d[i-1] <= d[i-3]:
                return True
            # case 2: current line overlaps/touches line i-4
            if i >= 4 and d[i-1] == d[i-3] and d[i] + d[i-4] >= d[i-2]:
                return True
            # case 3: current line crosses line i-5 (spiral)
            if i >= 5 and d[i-2] >= d[i-4] and d[i] + d[i-4] >= d[i-2] and d[i-1] <= d[i-3] and d[i-1] + d[i-5] >= d[i-3]:
                return True
        return False