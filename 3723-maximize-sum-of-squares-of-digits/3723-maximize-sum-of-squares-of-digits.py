class Solution(object):
    def maxSumOfSquares(self, num, sum):
        if sum > 9 * num:
            return ""
        nines, rem = divmod(sum, 9)
        res = "9" * nines
        if rem:
            res += str(rem)
        return res + "0" * (num - len(res))