1class Solution(object):
2    def climbStairs(self, n):
3        """
4        :type n: int
5        :rtype: int
6        """
7        if n <= 2:
8            return n
9        
10        prev2 = 1  # ways to reach step i-2
11        prev1 = 2  # ways to reach step i-1
12        
13        for i in range(3, n + 1):
14            curr = prev1 + prev2
15            prev2 = prev1
16            prev1 = curr
17        
18        return prev1