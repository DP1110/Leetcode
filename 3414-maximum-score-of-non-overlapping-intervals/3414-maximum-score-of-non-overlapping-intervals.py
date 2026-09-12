import bisect

class Solution(object):
    def maximumWeight(self, intervals):
        n = len(intervals)
        o = sorted(range(n), key=lambda i: intervals[i][1])
        sorted_r = [intervals[i][1] for i in o]

        def better(a, b):
            if a[0] != b[0]:
                return a if a[0] > b[0] else b
            if a[1] is None:
                return b
            if b[1] is None:
                return a
            return a if a[1] <= b[1] else b

        dp = [[(0, ())] + [(-1, None)] * 4 for _ in range(n + 1)]

        for t in range(1, n + 1):
            idx0 = o[t - 1]
            l, r, w = intervals[idx0][0], intervals[idx0][1], intervals[idx0][2]
            p = bisect.bisect_left(sorted_r, l) - 1
            prefix = p + 1
            row = [dp[t - 1][0]]
            for k in range(1, 5):
                skip_opt = dp[t - 1][k]
                prev = dp[prefix][k - 1]
                if prev[1] is not None:
                    new_score = prev[0] + w
                    new_indices = tuple(sorted(prev[1] + (idx0,)))
                    take_opt = (new_score, new_indices)
                else:
                    take_opt = (-1, None)
                row.append(better(skip_opt, take_opt))
            dp[t] = row

        best = dp[n][0]
        for k in range(1, 5):
            best = better(best, dp[n][k])

        return list(best[1]) if best[1] is not None else []