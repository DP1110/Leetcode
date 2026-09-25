class Solution(object):
    def braceExpansionII(self, expression):
        self.s = expression
        self.i = 0
        result = self.parse_union()
        return sorted(result)

    def parse_union(self):
        sets = [self.parse_concat()]
        while self.i < len(self.s) and self.s[self.i] == ',':
            self.i += 1
            sets.append(self.parse_concat())
        res = set()
        for s in sets:
            res |= s
        return res

    def parse_concat(self):
        result = {""}
        while self.i < len(self.s) and self.s[self.i] not in ',}':
            term = self.parse_term()
            result = {a + b for a in result for b in term}
        return result

    def parse_term(self):
        if self.s[self.i] == '{':
            self.i += 1
            res = self.parse_union()
            self.i += 1  # skip '}'
            return res
        else:
            c = self.s[self.i]
            self.i += 1
            return {c}