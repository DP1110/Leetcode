1class Solution(object):
2    def convertToTitle(self, columnNumber):
3        """
4        :type columnNumber: int
5        :rtype: str
6        """
7        result = []
8        n = columnNumber
9
10        while n > 0:
11            n -= 1
12            rem = n % 26
13            result.append(chr(ord('A') + rem))
14            n = n // 26
15
16        return ''.join(reversed(result))