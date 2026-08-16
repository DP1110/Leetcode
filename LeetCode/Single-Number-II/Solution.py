1class Solution:
2    def singleNumber(self, nums):
3        ones, twos = 0, 0
4        for n in nums:
5            ones = (ones ^ n) & ~twos
6            twos = (twos ^ n) & ~ones
7        return ones