class Solution(object):
    def digitSum(self, s, k):
    
        while len(s) > k:
            s = "".join(
                str(sum(map(int, s[i:i+k])))
                for i in range(0, len(s), k)
            )
        return s
        