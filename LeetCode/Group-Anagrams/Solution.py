1class Solution:
2    def groupAnagrams(self, strs):
3        groups = {}
4        
5        for s in strs:
6            key = "".join(sorted(s))
7            groups.setdefault(key, []).append(s)
8        
9        return list(groups.values())