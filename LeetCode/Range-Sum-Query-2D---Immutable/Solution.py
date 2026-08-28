1class NumMatrix(object):
2    def __init__(self, matrix):
3        m, n = len(matrix), len(matrix[0])
4        self.pre = [[0] * (n + 1) for _ in range(m + 1)]
5        for i in range(m):
6            for j in range(n):
7                self.pre[i+1][j+1] = matrix[i][j] + self.pre[i][j+1] + self.pre[i+1][j] - self.pre[i][j]
8
9    def sumRegion(self, row1, col1, row2, col2):
10        pre = self.pre
11        return pre[row2+1][col2+1] - pre[row1][col2+1] - pre[row2+1][col1] + pre[row1][col1]