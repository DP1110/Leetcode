class Solution(object):
    def distinctSubseqII(self, s):
        MOD = 10 ** 9 + 7
        dp = [0] * 26
        total = 0
        for c in s:
            idx = ord(c) - ord('a')
            new_total = (total * 2 + 1) % MOD
            new_total = (new_total - dp[idx]) % MOD
            dp[idx] = (total + 1) % MOD
            total = new_total
        return total % MOD