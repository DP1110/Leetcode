1class Solution(object):
2    def maxPoints(self, points):
3        """
4        :type points: List[List[int]]
5        :rtype: int
6        """
7        n = len(points)
8        if n <= 2:
9            return n
10
11        def gcd(a, b):
12            while b:
13                a, b = b, a % b
14            return a
15
16        best = 1
17
18        for i in range(n):
19            slopes = {}
20            x1, y1 = points[i][0], points[i][1]
21            local_max = 0
22
23            for j in range(n):
24                if j == i:
25                    continue
26                x2, y2 = points[j][0], points[j][1]
27                dx = x2 - x1
28                dy = y2 - y1
29
30                if dx == 0:
31                    key = ('inf',)
32                elif dy == 0:
33                    key = (0,)
34                else:
35                    g = gcd(abs(dx), abs(dy))
36                    dx //= g
37                    dy //= g
38                    if dx < 0:
39                        dx = -dx
40                        dy = -dy
41                    key = (dx, dy)
42
43                slopes[key] = slopes.get(key, 0) + 1
44                if slopes[key] > local_max:
45                    local_max = slopes[key]
46
47            best = max(best, local_max + 1)
48
49        return best