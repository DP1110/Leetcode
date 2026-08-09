1class Solution:
2    def plusOne(self, digits: list[int]) -> list[int]:
3        n = len(digits)
4        for i in range(n - 1, -1, -1):
5            if digits[i] < 9:
6                digits[i] += 1
7                return digits
8            digits[i] = 0
9        return [1] + [0] * n