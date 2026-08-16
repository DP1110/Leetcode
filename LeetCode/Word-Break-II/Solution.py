1class Solution:
2    def wordBreak(self, s, wordDict):
3        word_set = set(wordDict)
4        memo = {}
5
6        def backtrack(start):
7            if start == len(s):
8                return [""]
9            if start in memo:
10                return memo[start]
11
12            sentences = []
13            for end in range(start + 1, len(s) + 1):
14                word = s[start:end]
15                if word in word_set:
16                    rest = backtrack(end)
17                    for r in rest:
18                        sentences.append(word + ("" if r == "" else " " + r))
19
20            memo[start] = sentences
21            return sentences
22
23        return backtrack(0)