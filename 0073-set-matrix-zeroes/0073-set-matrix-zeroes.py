class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        
        m, n = len(matrix), len(matrix[0])
        first_col_zero = False
        
        # 1. Check if first column needs to be zeroed
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
        
        # 2. Use first row and first column as markers
        for i in range(m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # 3. Zero out cells based on markers (skip first row & col)
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # 4. Handle first row
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
        
        # 5. Handle first column
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0