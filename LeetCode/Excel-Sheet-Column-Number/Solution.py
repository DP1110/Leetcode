1class Solution(object):
2    def titleToNumber(self, columnTitle):
3        """
4        :type columnTitle: str
5        :rtype: int
6        """
7        result = 0
8
9        for ch in columnTitle:
10            result = result * 26 + (ord(ch) - ord('A') + 1)
11
12        return result