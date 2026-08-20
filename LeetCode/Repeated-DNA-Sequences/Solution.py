1class Solution(object):
2    def findRepeatedDnaSequences(self, s):
3        seen = set()
4        rep = set()
5        for i in range(len(s) - 9):
6            sub = s[i:i+10]
7            if sub in seen:
8                rep.add(sub)
9            else:
10                seen.add(sub)
11        return list(rep)