class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()  # splits on any whitespace run, drops empties
        words.reverse()
        return ' '.join(words)