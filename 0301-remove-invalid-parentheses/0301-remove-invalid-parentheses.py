class Solution(object):
    def removeInvalidParentheses(self, s):
        def is_valid(st):
            bal = 0
            for c in st:
                if c == '(':
                    bal += 1
                elif c == ')':
                    bal -= 1
                    if bal < 0:
                        return False
            return bal == 0

        level = {s}
        while True:
            valid = [x for x in level if is_valid(x)]
            if valid:
                return valid
            nxt = set()
            for x in level:
                for i in range(len(x)):
                    if x[i] in '()':
                        nxt.add(x[:i] + x[i+1:])
            level = nxt