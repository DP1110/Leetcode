1import heapq
2
3class Solution(object):
4    def getSkyline(self, buildings):
5        events = []
6        for l, r, h in buildings:
7            events.append((l, -h, r))
8            events.append((r, 0, 0))
9        events.sort()
10
11        res = []
12        heap = [(0, float('inf'))]
13        for x, negh, r in events:
14            while heap[0][1] <= x:
15                heapq.heappop(heap)
16            if negh:
17                heapq.heappush(heap, (negh, r))
18            cur_height = -heap[0][0]
19            if not res or res[-1][1] != cur_height:
20                res.append([x, cur_height])
21        return res