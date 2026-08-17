1class Solution(object):
2    def reverseWords(self, s):
3        """
4        :type s: str
5        :rtype: str
6        """
7        words = s.split()  # splits on any whitespace run, drops empties
8        words.reverse()
9        return ' '.join(words)