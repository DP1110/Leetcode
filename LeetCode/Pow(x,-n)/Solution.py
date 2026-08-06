1class Solution:
2    def myPow(self, x, n):
3        # Handle negative exponent
4        if n < 0:
5            x = 1 / x
6            n = -n
7        
8        result = 1
9        
10        while n:
11            # If n is odd, multiply result by current x
12            if n & 1:
13                result *= x
14            
15            # Square x and halve n
16            x *= x
17            n >>= 1
18        
19        return result