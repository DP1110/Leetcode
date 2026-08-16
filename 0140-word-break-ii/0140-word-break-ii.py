class Solution:
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)
        memo = {}

        def backtrack(start):
            if start == len(s):
                return [""]
            if start in memo:
                return memo[start]

            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    rest = backtrack(end)
                    for r in rest:
                        sentences.append(word + ("" if r == "" else " " + r))

            memo[start] = sentences
            return sentences

        return backtrack(0)