from collections import Counter

class Solution(object):
    def getHint(self, secret, guess):
        bulls = sum(s == g for s, g in zip(secret, guess))
        cs = Counter(secret)
        cg = Counter(guess)
        both = sum((cs & cg).values())
        cows = both - bulls
        return "%dA%dB" % (bulls, cows)