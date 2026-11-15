class Solution:
    def numOfSubarrays(self, arr):
        MOD = 10**9 + 7
        even, odd = 1, 0
        parity = 0
        ans = 0
        for x in arr:
            parity ^= (x & 1)
            if parity == 0:
                ans += odd
                even += 1
            else:
                ans += even
                odd += 1
        return ans % MOD