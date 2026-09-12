class Solution(object):
    def findTheDifference(self, s, t):
        result = 0
        for c in s + t:
            result ^= ord(c)
        return chr(result)