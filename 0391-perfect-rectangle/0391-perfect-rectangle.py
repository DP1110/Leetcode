class Solution(object):
    def isRectangleCover(self, rectangles):
        area = 0
        corners = set()
        min_x = min_y = float('inf')
        max_x = max_y = float('-inf')

        for x1, y1, x2, y2 in rectangles:
            area += (x2 - x1) * (y2 - y1)
            min_x, min_y = min(min_x, x1), min(min_y, y1)
            max_x, max_y = max(max_x, x2), max(max_y, y2)

            for pt in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if pt in corners:
                    corners.remove(pt)
                else:
                    corners.add(pt)

        if area != (max_x - min_x) * (max_y - min_y):
            return False

        if len(corners) != 4:
            return False

        expected = {(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)}
        return corners == expected