class Solution(object):
    def findRepeatedDnaSequences(self, s):
        seen = set()
        rep = set()
        for i in range(len(s) - 9):
            sub = s[i:i+10]
            if sub in seen:
                rep.add(sub)
            else:
                seen.add(sub)
        return list(rep)