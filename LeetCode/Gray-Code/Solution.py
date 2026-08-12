1class Solution(object):
2    def grayCode(self, n):
3        result = [0]
4        for i in range(n):
5            # Reflect and add the new bit
6            add = 1 << i
7            for j in range(len(result) - 1, -1, -1):
8                result.append(result[j] + add)
9        return result