import random

class Solution:
    def smallestUniqueSubarray(self, nums):
        n = len(nums)
        M = (1 << 61) - 1
        B = random.randrange(10 ** 6, M - 1)

        H = [0] * (n + 1)
        pw = [1] * (n + 1)
        for i in range(n):
            H[i + 1] = (H[i] * B + nums[i]) % M
            pw[i + 1] = (pw[i] * B) % M

        def has_unique(L):
            cnt = {}
            p = pw[L]
            for i in range(n - L + 1):
                h = (H[i + L] - H[i] * p) % M
                cnt[h] = cnt.get(h, 0) + 1
            for v in cnt.values():
                if v == 1:
                    return True
            return False

        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if has_unique(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo