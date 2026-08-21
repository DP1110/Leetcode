1class Solution(object):
2    def countPrimes(self, n):
3        if n < 3:
4            return 0
5        sieve = bytearray([1]) * n
6        sieve[0] = sieve[1] = 0
7        for i in range(2, int(n ** 0.5) + 1):
8            if sieve[i]:
9                sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
10        return sum(sieve)