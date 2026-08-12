1from collections import Counter
2
3class Solution(object):
4    def minimumPushes(self, word):
5        # Count frequency of each letter
6        freq = Counter(word)
7        
8        # Sort frequencies descending
9        frequencies = sorted(freq.values(), reverse=True)
10        
11        total = 0
12        for i, count in enumerate(frequencies):
13            # i // 8 tells us which "layer" the letter is in
14            # 0-7 → 1 push, 8-15 → 2 pushes, 16-23 → 3 pushes, 24+ → 4 pushes
15            pushes = (i // 8) + 1
16            total += count * pushes
17        
18        return total