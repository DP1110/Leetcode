class Solution:
    def evaluate(self, s, knowledge):
        d = dict(knowledge)
        res = []
        i, n = 0, len(s)
        while i < n:
            if s[i] == '(':
                j = s.find(')', i)
                key = s[i+1:j]
                res.append(d.get(key, '?'))
                i = j + 1
            else:
                res.append(s[i])
                i += 1
        return ''.join(res)