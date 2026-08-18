class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = []
        n = columnNumber

        while n > 0:
            n -= 1
            rem = n % 26
            result.append(chr(ord('A') + rem))
            n = n // 26

        return ''.join(reversed(result))