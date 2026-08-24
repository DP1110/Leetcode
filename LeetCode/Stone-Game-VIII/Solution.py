1class Solution(object):
2    def stoneGameVIII(self, stones):
3        """
4        :type stones: List[int]
5        :rtype: int
6        """
7        n = len(stones)
8        P = [0]*n
9        P[0] = stones[0]
10        for i in xrange(1, n):
11            P[i] = P[i-1] + stones[i]
12        dp = P[n-1]
13        for i in xrange(n-2, 0, -1):
14            dp = max(P[i]-dp, dp)
15        return dp