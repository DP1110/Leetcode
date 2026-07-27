class Solution(object):
    def reverse(self, x):
        INT_MAX = 2147483647   # 2^31 - 1
        INT_MIN = -2147483648  # -2^31
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        
        while x != 0:
            pop = x % 10
            x //= 10
            
            # Overflow check BEFORE multiplying rev by 10
            # INT_MAX = 2147483647, so last digit must be ≤ 7 when rev == 214748364
            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and pop > 7):
                return 0
            
            rev = rev * 10 + pop
        
        return sign * rev