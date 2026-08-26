1class Solution(object):
2    def addDigits(self, num):
3        if num == 0:
4            return 0
5        return 1 + (num - 1) % 9
6        