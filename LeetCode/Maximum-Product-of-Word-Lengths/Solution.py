1class Solution(object):
2    def maxProduct(self, words):
3        n = len(words)
4        masks = [0] * n
5        for i, w in enumerate(words):
6            for c in w:
7                masks[i] |= 1 << (ord(c) - ord('a'))
8
9        best = 0
10        for i in range(n):
11            for j in range(i + 1, n):
12                if masks[i] & masks[j] == 0:
13                    best = max(best, len(words[i]) * len(words[j]))
14        return best