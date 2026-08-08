class Solution:
    def validSequence(self, word1, word2):
        n, m = len(word1), len(word2)
        suff = [0] * (n + 1)
        p = m - 1
        for i in range(n - 1, -1, -1):
            suff[i] = suff[i + 1]
            if p >= 0 and word1[i] == word2[p]:
                suff[i] += 1
                p -= 1

        res = []
        j = 0
        changed = False
        i = 0
        while i < n and j < m:
            if word1[i] == word2[j]:
                res.append(i)
                j += 1
                i += 1
            elif not changed and suff[i+1] >= m - j - 1:
                res.append(i)
                changed = True
                j += 1
                i += 1
            else:
                i += 1

        return res if j == m else []