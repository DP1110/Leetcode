1class Solution(object):
2    def searchMatrix(self, matrix, target):
3        """
4        :type matrix: List[List[int]]
5        :type target: int
6        :rtype: bool
7        """
8        if not matrix or not matrix[0]:
9            return False
10        rows = len(matrix)
11        cols = len(matrix[0])
12        r, c = 0, cols-1
13        while r < rows and c >= 0:
14            v = matrix[r][c]
15            if v == target:
16                return True
17            elif v > target:
18                c -= 1
19            else:
20                r += 1
21        return False