class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        # Use the shortest string as the reference
        shortest = min(strs, key=len)
        
        for i, char in enumerate(shortest):
            # Check this character against the same position in every other string
            for string in strs:
                if string[i] != char:
                    return shortest[:i]
        
        # All characters of the shortest string matched
        return shortest