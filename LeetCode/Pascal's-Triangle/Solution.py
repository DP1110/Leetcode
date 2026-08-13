1class Solution:
2    def generate(self, numRows):
3        result = []
4        for i in range(numRows):
5            row = [1] * (i + 1)
6            for j in range(1, i):
7                row[j] = result[i - 1][j - 1] + result[i - 1][j]
8            result.append(row)
9        return result