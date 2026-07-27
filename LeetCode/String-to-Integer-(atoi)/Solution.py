1class Solution(object):
2    def myAtoi(self, s):
3        INT_MAX = 2147483647
4        INT_MIN = -2147483648
5        BOUND = 214748364   # INT_MAX // 10
6        
7        i, n = 0, len(s)
8        
9        # Step 1: Skip leading whitespace
10        while i < n and s[i] == ' ':
11            i += 1
12        
13        # Step 2: Determine sign
14        sign = 1
15        if i < n and s[i] in '+-':
16            sign = -1 if s[i] == '-' else 1
17            i += 1
18        
19        # Step 3 & 4: Read digits with overflow check
20        result = 0
21        while i < n and '0' <= s[i] <= '9':
22            digit = ord(s[i]) - ord('0')
23            
24            # Check if next step would overflow
25            if result > BOUND:
26                return INT_MAX if sign == 1 else INT_MIN
27            
28            if result == BOUND:
29                # Positive limit: 2147483647, so last digit ≤ 7
30                if sign == 1 and digit > 7:
31                    return INT_MAX
32                # Negative limit: -2147483648, so last digit ≤ 8
33                if sign == -1 and digit > 8:
34                    return INT_MIN
35            
36            result = result * 10 + digit
37            i += 1
38        
39        # Step 5: Apply sign
40        return sign * result