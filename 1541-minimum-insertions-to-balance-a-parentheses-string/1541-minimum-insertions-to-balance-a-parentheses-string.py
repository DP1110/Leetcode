class Solution(object):
    def minInsertions(self, s):
        res = 0
        need = 0  # right parens still needed
        for c in s:
            if c == '(':
                if need % 2 == 1:
                    res += 1
                    need -= 1
                need += 2
            else:
                need -= 1
                if need < 0:
                    res += 1
                    need += 2
        return res + need