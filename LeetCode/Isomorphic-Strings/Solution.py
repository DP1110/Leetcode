1class Solution(object):
2    def isIsomorphic(self, s, t):
3        map_st, map_ts = {}, {}
4        for a, b in zip(s, t):
5            if a in map_st and map_st[a] != b:
6                return False
7            if b in map_ts and map_ts[b] != a:
8                return False
9            map_st[a] = b
10            map_ts[b] = a
11        return True