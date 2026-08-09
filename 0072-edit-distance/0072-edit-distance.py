class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        
        # prev[j] = edit distance between word1[:i-1] and word2[:j]
        prev = range(n + 1)  # base case: converting empty word1 to word2[:j] needs j inserts
        
        for i in range(1, m + 1):
            curr = [i] * (n + 1)  # base case: converting word1[:i] to empty word2 needs i deletes
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]  # no operation needed
                else:
                    # delete: prev[j], insert: curr[j-1], replace: prev[j-1]
                    curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])
            prev = curr
        
        return prev[n]