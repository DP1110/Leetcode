1class Solution(object):
2    def isAnagram(self, s, t):
3        """
4        :type s: str
5        :type t: str
6        :rtype: bool
7        """
8        if len(s) != len(t):
9            return False
10        count = [0]*26
11        for c in s:
12            count[ord(c)-ord('a')] += 1
13        for c in t:
14            count[ord(c)-ord('a')] -= 1
15        for x in count:
16            if x != 0:
17                return False
18        return True