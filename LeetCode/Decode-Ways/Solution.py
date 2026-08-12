1class Solution(object):
2    def numDecodings(self, s):
3        if not s or s[0] == '0':
4            return 0
5        
6        n = len(s)
7        prev2 = 1  # dp[i-2]
8        prev1 = 1  # dp[i-1]
9        
10        for i in range(1, n):
11            current = 0
12            
13            # Single digit: s[i] must not be '0'
14            if s[i] != '0':
15                current += prev1
16            
17            # Two digits: s[i-1:i+1] must be between 10 and 26
18            two_digit = int(s[i-1:i+1])
19            if 10 <= two_digit <= 26:
20                current += prev2
21            
22            prev2 = prev1
23            prev1 = current
24        
25        return prev1