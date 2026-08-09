1class Solution(object):
2    def minDistance(self, word1, word2):
3        """
4        :type word1: str
5        :type word2: str
6        :rtype: int
7        """
8        m, n = len(word1), len(word2)
9        
10        # prev[j] = edit distance between word1[:i-1] and word2[:j]
11        prev = range(n + 1)  # base case: converting empty word1 to word2[:j] needs j inserts
12        
13        for i in range(1, m + 1):
14            curr = [i] * (n + 1)  # base case: converting word1[:i] to empty word2 needs i deletes
15            for j in range(1, n + 1):
16                if word1[i - 1] == word2[j - 1]:
17                    curr[j] = prev[j - 1]  # no operation needed
18                else:
19                    # delete: prev[j], insert: curr[j-1], replace: prev[j-1]
20                    curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])
21            prev = curr
22        
23        return prev[n]