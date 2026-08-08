class Solution:
    def myPow(self, x, n):
        # Handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1
        
        while n:
            # If n is odd, multiply result by current x
            if n & 1:
                result *= x
            
            # Square x and halve n
            x *= x
            n >>= 1
        
        return result