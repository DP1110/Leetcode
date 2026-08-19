import functools

class Solution(object):
    def largestNumber(self, nums):
        strs = map(str, nums)
        strs.sort(cmp=lambda a, b: cmp(b + a, a + b))
        result = ''.join(strs)
        return '0' if result[0] == '0' else result