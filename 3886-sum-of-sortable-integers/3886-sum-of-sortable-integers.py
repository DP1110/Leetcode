class Solution(object):
    def sortableIntegers(self, nums):
        n = len(nums)
        pre = [0] * (n + 1)  # pre[i] = descents at indices < i
        for j in range(n - 1):
            pre[j + 1] = pre[j] + (1 if nums[j] > nums[j + 1] else 0)
        pre[n] = pre[n - 1] if n > 0 else 0
        nd = [n] * (n + 1)  # next descent index >= j
        for j in range(n - 2, -1, -1):
            nd[j] = j if nums[j] > nums[j + 1] else nd[j + 1]

        res = 0
        for k in range(1, n + 1):
            if n % k:
                continue
            ok = True
            prev_max = 0
            for s in range(0, n, k):
                e = s + k - 1
                lin = pre[e] - pre[s]  # descents at s..e-1
                wrap = 1 if nums[e] > nums[s] else 0
                if lin + wrap > 1 and not (lin == 0 and wrap == 1 and False):
                    ok = False
                    break
                if lin == 0:
                    lo, hi = nums[s], nums[e]
                    if wrap == 1:
                        pass  # sorted block, fine
                else:
                    p = nd[s]
                    lo, hi = nums[p + 1], nums[p]
                if lo < prev_max:
                    ok = False
                    break
                prev_max = hi
            if ok:
                res += k
        return res