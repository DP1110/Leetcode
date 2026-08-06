class Solution:
    def isMatch(self, s, p):
        i = j = 0
        star = -1      # Position of last '*' in p
        match = 0      # Position in s corresponding to star's match
        
        while i < len(s):
            # Exact match or '?'
            if j < len(p) and (p[j] == '?' or p[j] == s[i]):
                i += 1
                j += 1
            # '*' - record position, advance pattern only
            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1
            # Mismatch, but we have a '*' to backtrack to
            elif star != -1:
                j = star + 1      # Reset pattern to after '*'
                match += 1        # Use '*' to consume one more char
                i = match
            # Mismatch and no '*' to save us
            else:
                return False
        
        # Skip trailing '*' in pattern
        while j < len(p) and p[j] == '*':
            j += 1
        
        return j == len(p)