class Solution(object):
    def restoreIpAddresses(self, s):
        result = []
        n = len(s)
        
        # i, j, k are the positions of the 3 dots
        # Segment 1: s[0:i], Segment 2: s[i:j], Segment 3: s[j:k], Segment 4: s[k:n]
        for i in range(1, min(4, n)):
            for j in range(i + 1, min(i + 4, n)):
                for k in range(j + 1, min(j + 4, n)):
                    a, b, c, d = s[0:i], s[i:j], s[j:k], s[k:n]
                    
                    if self.isValid(a) and self.isValid(b) and self.isValid(c) and self.isValid(d):
                        result.append(a + '.' + b + '.' + c + '.' + d)
        
        return result
    
    def isValid(self, seg):
        # Length check: empty or >3 is invalid
        if len(seg) == 0 or len(seg) > 3:
            return False
        # Leading zero check
        if seg[0] == '0' and len(seg) > 1:
            return False
        # Value check
        return int(seg) <= 255