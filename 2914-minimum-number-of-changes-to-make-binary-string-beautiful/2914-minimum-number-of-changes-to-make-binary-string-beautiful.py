class Solution:
    def minChanges(self, s):
        res = 0
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                res += 1
        return res