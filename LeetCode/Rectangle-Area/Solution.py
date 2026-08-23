1class Solution(object):
2    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
3        areaA = (ax2 - ax1) * (ay2 - ay1)
4        areaB = (bx2 - bx1) * (by2 - by1)
5
6        overlap_x = max(0, min(ax2, bx2) - max(ax1, bx1))
7        overlap_y = max(0, min(ay2, by2) - max(ay1, by1))
8        overlap = overlap_x * overlap_y
9
10        return areaA + areaB - overlap