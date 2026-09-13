from collections import defaultdict

class Solution(object):
    def largestOverlap(self, img1, img2):
        n = len(img1)
        pts1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c]]
        pts2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c]]

        shift_count = defaultdict(int)
        for r1, c1 in pts1:
            for r2, c2 in pts2:
                shift_count[(r1 - r2, c1 - c2)] += 1

        return max(shift_count.values()) if shift_count else 0