class Solution:
    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Edge case: overflow when -2^31 / -1 = 2^31
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine if result is negative
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with positive values
        dvd = abs(dividend)
        dvs = abs(divisor)
        
        quotient = 0
        
        while dvd >= dvs:
            temp = dvs
            multiple = 1
            
            # Double temp until it would exceed dvd
            while dvd >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            dvd -= temp
            quotient += multiple
        
        if negative:
            quotient = -quotient
        
        # Clamp to 32-bit signed integer range
        return min(max(quotient, INT_MIN), INT_MAX)