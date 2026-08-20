1class Solution(object):
2    def reverseBits(self, n):
3        res = 0
4        for i in range(32):
5            res = (res << 1) | (n & 1)
6            n >>= 1
7        return res