1class Solution(object):
2    def longestCommonPrefix(self, strs):
3        if not strs:
4            return ""
5        
6        # Use the shortest string as the reference
7        shortest = min(strs, key=len)
8        
9        for i, char in enumerate(shortest):
10            # Check this character against the same position in every other string
11            for string in strs:
12                if string[i] != char:
13                    return shortest[:i]
14        
15        # All characters of the shortest string matched
16        return shortest