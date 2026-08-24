1class Solution(object):
2    def isPowerOfTwo(self, n):
3        """
4        :type n: int
5        :rtype: bool
6        """
7        return n > 0 and (n & (n-1)) == 0