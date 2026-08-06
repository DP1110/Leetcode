1class Solution:
2    def isMatch(self, s, p):
3        i = j = 0
4        star = -1      # Position of last '*' in p
5        match = 0      # Position in s corresponding to star's match
6        
7        while i < len(s):
8            # Exact match or '?'
9            if j < len(p) and (p[j] == '?' or p[j] == s[i]):
10                i += 1
11                j += 1
12            # '*' - record position, advance pattern only
13            elif j < len(p) and p[j] == '*':
14                star = j
15                match = i
16                j += 1
17            # Mismatch, but we have a '*' to backtrack to
18            elif star != -1:
19                j = star + 1      # Reset pattern to after '*'
20                match += 1        # Use '*' to consume one more char
21                i = match
22            # Mismatch and no '*' to save us
23            else:
24                return False
25        
26        # Skip trailing '*' in pattern
27        while j < len(p) and p[j] == '*':
28            j += 1
29        
30        return j == len(p)