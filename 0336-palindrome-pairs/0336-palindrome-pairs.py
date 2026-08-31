class Solution(object):
    def palindromePairs(self, words):
        word_idx = {w: i for i, w in enumerate(words)}
        res = []

        for i, w in enumerate(words):
            n = len(w)
            for j in range(n + 1):
                prefix = w[:j]
                suffix = w[j:]
                # case A: prefix is palindrome, reversed suffix exists elsewhere -> rev_suffix + w
                if prefix == prefix[::-1]:
                    rev_suffix = suffix[::-1]
                    if rev_suffix in word_idx and word_idx[rev_suffix] != i:
                        res.append([word_idx[rev_suffix], i])
                # case B: suffix is palindrome, reversed prefix exists -> w + rev_prefix
                if j != n and suffix == suffix[::-1]:
                    rev_prefix = prefix[::-1]
                    if rev_prefix in word_idx and word_idx[rev_prefix] != i:
                        res.append([i, word_idx[rev_prefix]])

        return res