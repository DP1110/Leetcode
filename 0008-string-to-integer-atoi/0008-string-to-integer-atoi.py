class Solution(object):
    def myAtoi(self, s):
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        BOUND = 214748364   # INT_MAX // 10
        
        i, n = 0, len(s)
        
        # Step 1: Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # Step 2: Determine sign
        sign = 1
        if i < n and s[i] in '+-':
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        # Step 3 & 4: Read digits with overflow check
        result = 0
        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')
            
            # Check if next step would overflow
            if result > BOUND:
                return INT_MAX if sign == 1 else INT_MIN
            
            if result == BOUND:
                # Positive limit: 2147483647, so last digit ≤ 7
                if sign == 1 and digit > 7:
                    return INT_MAX
                # Negative limit: -2147483648, so last digit ≤ 8
                if sign == -1 and digit > 8:
                    return INT_MIN
            
            result = result * 10 + digit
            i += 1
        
        # Step 5: Apply sign
        return sign * result