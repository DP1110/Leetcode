class Solution(object):
    def singleNumber(self, nums):
        xor_all = 0
        for n in nums:
            xor_all ^= n
        diff = xor_all & (-xor_all)
        a = 0
        for n in nums:
            if n & diff:
                a ^= n
        b = xor_all ^ a
        return [a, b]