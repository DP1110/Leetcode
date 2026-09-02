import bisect

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        m, n = len(matrix), len(matrix[0])
        best = float('-inf')

        for top in range(m):
            col_sum = [0] * n
            for bottom in range(top, m):
                for c in range(n):
                    col_sum[c] += matrix[bottom][c]

                # find max subarray sum <= k in col_sum using prefix sums + sorted list
                prefix = 0
                sorted_prefixes = [0]
                for x in col_sum:
                    prefix += x
                    idx = bisect.bisect_left(sorted_prefixes, prefix - k)
                    if idx < len(sorted_prefixes):
                        best = max(best, prefix - sorted_prefixes[idx])
                    bisect.insort(sorted_prefixes, prefix)

        return best

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna