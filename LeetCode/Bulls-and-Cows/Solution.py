1from collections import Counter
2
3class Solution(object):
4    def getHint(self, secret, guess):
5        bulls = sum(s == g for s, g in zip(secret, guess))
6        cs = Counter(secret)
7        cg = Counter(guess)
8        both = sum((cs & cg).values())
9        cows = both - bulls
10        return "%dA%dB" % (bulls, cows)