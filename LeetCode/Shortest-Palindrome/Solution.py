1class Solution(object):
2    def shortestPalindrome(self, s):
3        if not s:
4            return s
5        rev = s[::-1]
6        combined = s + '#' + rev
7        n = len(combined)
8        fail = [0] * n
9        for i in range(1, n):
10            j = fail[i-1]
11            while j > 0 and combined[i] != combined[j]:
12                j = fail[j-1]
13            if combined[i] == combined[j]:
14                j += 1
15            fail[i] = j
16        overlap = fail[-1]
17        return rev[:len(s)-overlap] + s