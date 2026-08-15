class Solution:
    def getRow(self, rowIndex):
        row = [1] * (rowIndex + 1)
        
        for i in range(1, rowIndex + 1):
            # Update from right to left to avoid overwriting
            for j in range(i - 1, 0, -1):
                row[j] = row[j] + row[j - 1]
        
        return row