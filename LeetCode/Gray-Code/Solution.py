1class Solution(object):
2    def grayCode(self, n):
3        """
4        :type n: int
5        :rtype: List[int]
6        """
7        result = []
8        size = 1 << n  # 2^n
9        
10        for i in range(size):
11            result.append(i ^ (i >> 1))
12        
13        return result