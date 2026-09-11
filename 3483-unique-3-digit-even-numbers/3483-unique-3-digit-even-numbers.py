from collections import Counter
from itertools import permutations

class Solution(object):
    def totalNumbers(self, digits):
        seen = set()
        for p in set(permutations(digits, 3)):
            if p[0] != 0 and p[2] % 2 == 0:
                seen.add(p)
        return len(seen)