1class Solution(object):
2    def singleNumber(self, nums):
3        xor_all = 0
4        for n in nums:
5            xor_all ^= n
6        diff = xor_all & (-xor_all)
7        a = 0
8        for n in nums:
9            if n & diff:
10                a ^= n
11        b = xor_all ^ a
12        return [a, b]