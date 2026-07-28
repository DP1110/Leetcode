1class Solution(object):
2    def isMatch(self, s, p):
3        m, n = len(s), len(p)
4        # dp[i][j] = does s[0:i] match p[0:j]?
5        dp = [[False] * (n + 1) for _ in range(m + 1)]
6        
7        # Empty string matches empty pattern
8        dp[0][0] = True
9        
10        # Handle patterns like a*, a*b*, a*b*c* matching empty string
11        for j in range(2, n + 1):
12            if p[j - 1] == '*':
13                dp[0][j] = dp[0][j - 2]
14        
15        for i in range(1, m + 1):
16            for j in range(1, n + 1):
17                if p[j - 1] == '*':
18                    # Option 1: zero occurrences of p[j-2]
19                    dp[i][j] = dp[i][j - 2]
20                    
21                    # Option 2: one or more occurrences
22                    # Check if s[i-1] matches p[j-2] (the char before *)
23                    if self._match(s[i - 1], p[j - 2]):
24                        dp[i][j] = dp[i][j] or dp[i - 1][j]
25                
26                else:
27                    # Direct character match or '.'
28                    if self._match(s[i - 1], p[j - 1]):
29                        dp[i][j] = dp[i - 1][j - 1]
30        
31        return dp[m][n]
32    
33    def _match(self, s_char, p_char):
34        return p_char == '.' or s_char == p_char