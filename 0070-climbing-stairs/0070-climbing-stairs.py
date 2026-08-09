class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        
        prev2 = 1  # ways to reach step i-2
        prev1 = 2  # ways to reach step i-1
        
        for i in range(3, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        
        return prev1