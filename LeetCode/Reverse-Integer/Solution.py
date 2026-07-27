1class Solution(object):
2    def reverse(self, x):
3        INT_MAX = 2147483647   # 2^31 - 1
4        INT_MIN = -2147483648  # -2^31
5        
6        sign = -1 if x < 0 else 1
7        x = abs(x)
8        rev = 0
9        
10        while x != 0:
11            pop = x % 10
12            x //= 10
13            
14            # Overflow check BEFORE multiplying rev by 10
15            # INT_MAX = 2147483647, so last digit must be ≤ 7 when rev == 214748364
16            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and pop > 7):
17                return 0
18            
19            rev = rev * 10 + pop
20        
21        return sign * rev