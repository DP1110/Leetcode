class Solution(object):
    def maxSum(self, nums, k):
        MOD = 10 ** 9 + 7
        bits = [0] * 30
        for x in nums:
            for b in range(30):
                if x >> b & 1:
                    bits[b] += 1

        res = 0
        for _ in range(k):
            v = 0
            for b in range(30):
                if bits[b] > 0:
                    v |= 1 << b
                    bits[b] -= 1
            res = (res + v * v) % MOD
        return res