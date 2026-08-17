class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        if n <= 2:
            return n

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        best = 1

        for i in range(n):
            slopes = {}
            x1, y1 = points[i][0], points[i][1]
            local_max = 0

            for j in range(n):
                if j == i:
                    continue
                x2, y2 = points[j][0], points[j][1]
                dx = x2 - x1
                dy = y2 - y1

                if dx == 0:
                    key = ('inf',)
                elif dy == 0:
                    key = (0,)
                else:
                    g = gcd(abs(dx), abs(dy))
                    dx //= g
                    dy //= g
                    if dx < 0:
                        dx = -dx
                        dy = -dy
                    key = (dx, dy)

                slopes[key] = slopes.get(key, 0) + 1
                if slopes[key] > local_max:
                    local_max = slopes[key]

            best = max(best, local_max + 1)

        return best