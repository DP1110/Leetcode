1class Solution(object):
2    def hIndex(self, citations):
3        n = len(citations)
4        buckets = [0] * (n + 1)
5        for c in citations:
6            buckets[min(c, n)] += 1
7        total = 0
8        for h in range(n, -1, -1):
9            total += buckets[h]
10            if total >= h:
11                return h
12        return 0