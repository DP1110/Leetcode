1import functools
2
3class Solution(object):
4    def largestNumber(self, nums):
5        strs = map(str, nums)
6        strs.sort(cmp=lambda a, b: cmp(b + a, a + b))
7        result = ''.join(strs)
8        return '0' if result[0] == '0' else result