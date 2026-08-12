class Solution(object):
    def minimumPushes(self, word):
        from collections import Counter
        
        # Count frequencies
        freq = Counter(word)
        
        # Sort frequencies in descending order
        frequencies = sorted(freq.values(), reverse=True)
        
        total = 0
        for i, count in enumerate(frequencies):
            # i//8 gives which "layer" (0-indexed), so pushes = i//8 + 1
            pushes = (i // 8) + 1
            total += count * pushes
        
        return total