1import heapq
2
3class MedianFinder(object):
4    def __init__(self):
5        self.lo = []  # max-heap (negated)
6        self.hi = []  # min-heap
7
8    def addNum(self, num):
9        heapq.heappush(self.lo, -num)
10        heapq.heappush(self.hi, -heapq.heappop(self.lo))
11        if len(self.hi) > len(self.lo):
12            heapq.heappush(self.lo, -heapq.heappop(self.hi))
13
14    def findMedian(self):
15        if len(self.lo) > len(self.hi):
16            return float(-self.lo[0])
17        return (-self.lo[0] + self.hi[0]) / 2.0