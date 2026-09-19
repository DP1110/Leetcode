class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        nx = max(x1, min(xCenter, x2))
        ny = max(y1, min(yCenter, y2))
        dx = xCenter - nx
        dy = yCenter - ny
        return dx * dx + dy * dy <= radius * radius