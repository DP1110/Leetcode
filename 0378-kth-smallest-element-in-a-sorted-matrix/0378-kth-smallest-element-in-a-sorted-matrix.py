class Solution(object):
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        lo, hi = matrix[0][0], matrix[n-1][n-1]

        def count_le(x):
            cnt = 0
            r, c = n - 1, 0
            while r >= 0 and c < n:
                if matrix[r][c] <= x:
                    cnt += r + 1
                    c += 1
                else:
                    r -= 1
            return cnt

        while lo < hi:
            mid = (lo + hi) // 2
            if count_le(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna