class Solution(object):
    def shortestPalindrome(self, s):
        if not s:
            return s
        rev = s[::-1]
        combined = s + '#' + rev
        n = len(combined)
        fail = [0] * n
        for i in range(1, n):
            j = fail[i-1]
            while j > 0 and combined[i] != combined[j]:
                j = fail[j-1]
            if combined[i] == combined[j]:
                j += 1
            fail[i] = j
        overlap = fail[-1]
        return rev[:len(s)-overlap] + s