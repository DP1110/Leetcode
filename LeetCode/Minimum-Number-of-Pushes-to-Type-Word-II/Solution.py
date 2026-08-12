1class Solution(object):
2    def minimumPushes(self, word):
3        from collections import Counter
4        
5        # Count frequencies
6        freq = Counter(word)
7        
8        # Sort frequencies in descending order
9        frequencies = sorted(freq.values(), reverse=True)
10        
11        total = 0
12        for i, count in enumerate(frequencies):
13            # i//8 gives which "layer" (0-indexed), so pushes = i//8 + 1
14            pushes = (i // 8) + 1
15            total += count * pushes
16        
17        return total