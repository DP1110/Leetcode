1class Solution(object):
2    def nthSuperUglyNumber(self, n, primes):
3        k = len(primes)
4        ugly = [1] * n
5        idx = [0] * k
6
7        for i in range(1, n):
8            candidates = [ugly[idx[j]] * primes[j] for j in range(k)]
9            nxt = min(candidates)
10            ugly[i] = nxt
11            for j in range(k):
12                if candidates[j] == nxt:
13                    idx[j] += 1
14        return ugly[n - 1]