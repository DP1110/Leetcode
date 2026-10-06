class Solution(object):
    def minAddToMakeValid(self, s):
        open_needed = 0
        close_needed = 0
        for c in s:
            if c == '(':
                open_needed += 1
            else:
                if open_needed > 0:
                    open_needed -= 1
                else:
                    close_needed += 1
        return open_needed + close_needed