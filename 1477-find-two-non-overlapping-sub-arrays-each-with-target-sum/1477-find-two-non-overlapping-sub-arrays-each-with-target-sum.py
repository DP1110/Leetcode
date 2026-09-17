class Solution(object):
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        best = [float('inf')] * n
        l = 0
        s = 0
        res = float('inf')
        min_len_so_far = float('inf')

        for r in range(n):
            s += arr[r]
            while s > target:
                s -= arr[l]
                l += 1
            if s == target:
                cur_len = r - l + 1
                if l > 0 and best[l-1] != float('inf'):
                    res = min(res, best[l-1] + cur_len)
                min_len_so_far = min(min_len_so_far, cur_len)
            best[r] = min_len_so_far

        return res if res != float('inf') else -1