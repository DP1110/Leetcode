class Solution(object):
    def grayCode(self, n):
        result = [0]
        for i in range(n):
            # Reflect and add the new bit
            add = 1 << i
            for j in range(len(result) - 1, -1, -1):
                result.append(result[j] + add)
        return result