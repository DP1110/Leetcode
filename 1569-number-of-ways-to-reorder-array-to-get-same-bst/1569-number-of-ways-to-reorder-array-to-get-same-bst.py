class Solution(object):
    def numOfWays(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv = [1] * (n + 1)
        inv[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            inv[i - 1] = inv[i] * i % MOD

        def C(a, b):
            return fact[a] * inv[b] % MOD * inv[a - b] % MOD

        res = 1
        stack = [nums]
        while stack:
            arr = stack.pop()
            if len(arr) <= 2:
                continue
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            res = res * C(len(arr) - 1, len(left)) % MOD
            stack.append(left)
            stack.append(right)
        return (res - 1) % MOD