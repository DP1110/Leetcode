1class Solution:
2    def lengthOfLastWord(self, s):
3        i = len(s) - 1
4        
5        # Skip trailing spaces
6        while i >= 0 and s[i] == ' ':
7            i -= 1
8        
9        # Count characters of the last word
10        length = 0
11        while i >= 0 and s[i] != ' ':
12            length += 1
13            i -= 1
14        
15        return length