class Solution(object):
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        # dp[i][j] = does s[0:i] match p[0:j]?
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty string matches empty pattern
        dp[0][0] = True
        
        # Handle patterns like a*, a*b*, a*b*c* matching empty string
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # Option 1: zero occurrences of p[j-2]
                    dp[i][j] = dp[i][j - 2]
                    
                    # Option 2: one or more occurrences
                    # Check if s[i-1] matches p[j-2] (the char before *)
                    if self._match(s[i - 1], p[j - 2]):
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                
                else:
                    # Direct character match or '.'
                    if self._match(s[i - 1], p[j - 1]):
                        dp[i][j] = dp[i - 1][j - 1]
        
        return dp[m][n]
    
    def _match(self, s_char, p_char):
        return p_char == '.' or s_char == p_char