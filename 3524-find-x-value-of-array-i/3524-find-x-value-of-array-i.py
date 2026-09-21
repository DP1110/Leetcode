class Solution(object):
    def resultArray(self, nums, k):
        result = [0] * k
        cur = [0] * k
        for x in nums:
            v = x % k
            new_cur = [0] * k
            for old_v in range(k):
                if cur[old_v]:
                    nv = (old_v * v) % k
                    new_cur[nv] += cur[old_v]
            new_cur[v] += 1
            cur = new_cur
            for xi in range(k):
                result[xi] += cur[xi]
        return result