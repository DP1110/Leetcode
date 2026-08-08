class Solution:
    def generateMatrix(self, n):
        matrix = [[0] * n for _ in range(n)]
        num = 1
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        
        while num <= n * n:
            # Left to right on top row
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1
            
            # Top to bottom on right column
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1
            
            # Right to left on bottom row
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1
            
            # Bottom to top on left column
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1
        
        return matrix