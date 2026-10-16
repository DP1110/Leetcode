class Solution(object):
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        B1 = [0] * (n + 2)
        B2 = [0] * (n + 2)

        def upd(B, i, v):
            while i <= n + 1:
                B[i] += v
                i += i & -i

        def qry(B, i):
            s = 0
            while i > 0:
                s += B[i]
                i -= i & -i
            return s

        def pref(i):  # sum d[1..i], 1-indexed
            return qry(B1, i) * i - qry(B2, i)

        last = {}
        cur = 0
        ans = 0
        for j in range(n):
            prev = last.get(nums[j], -1)
            l, r = prev + 2, j + 1  # 1-indexed [prev+1..j]
            s = pref(r) - pref(l - 1)
            cur += 2 * s + (r - l + 1)
            upd(B1, l, 1)
            upd(B1, r + 1, -1)
            upd(B2, l, l - 1)
            upd(B2, r + 1, -r)
            last[nums[j]] = j
            ans = (ans + cur) % MOD
        return ans