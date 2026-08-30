1class Solution(object):
2    def countRangeSum(self, nums, lower, upper):
3        prefix = [0] * (len(nums) + 1)
4        for i, x in enumerate(nums):
5            prefix[i + 1] = prefix[i] + x
6
7        def sort_count(lo, hi):
8            if hi - lo <= 1:
9                return 0
10            mid = (lo + hi) // 2
11            cnt = sort_count(lo, mid) + sort_count(mid, hi)
12
13            j = k = mid
14            for i in range(lo, mid):
15                while j < hi and prefix[j] - prefix[i] < lower:
16                    j += 1
17                while k < hi and prefix[k] - prefix[i] <= upper:
18                    k += 1
19                cnt += k - j
20
21            prefix[lo:hi] = sorted(prefix[lo:hi])
22            return cnt
23
24        return sort_count(0, len(prefix))