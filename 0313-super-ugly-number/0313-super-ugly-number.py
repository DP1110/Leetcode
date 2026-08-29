class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        k = len(primes)
        ugly = [1] * n
        idx = [0] * k

        for i in range(1, n):
            candidates = [ugly[idx[j]] * primes[j] for j in range(k)]
            nxt = min(candidates)
            ugly[i] = nxt
            for j in range(k):
                if candidates[j] == nxt:
                    idx[j] += 1
        return ugly[n - 1]