1class Solution:
2    def getRow(self, rowIndex):
3        row = [1] * (rowIndex + 1)
4        
5        for i in range(1, rowIndex + 1):
6            # Update from right to left to avoid overwriting
7            for j in range(i - 1, 0, -1):
8                row[j] = row[j] + row[j - 1]
9        
10        return row