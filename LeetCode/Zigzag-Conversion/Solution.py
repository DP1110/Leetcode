1class Solution(object):
2    def convert(self, s, numRows):
3        # Edge case: no zigzag possible
4        if numRows == 1 or numRows >= len(s):
5            return s
6        
7        # Create a list of strings, one per row
8        rows = [''] * numRows
9        current_row = 0
10        direction = 1  # 1 = going down, -1 = going up
11        
12        for char in s:
13            rows[current_row] += char
14            
15            # Flip direction at the boundaries
16            if current_row == 0:
17                direction = 1
18            elif current_row == numRows - 1:
19                direction = -1
20            
21            current_row += direction
22        
23        # Concatenate all rows
24        return ''.join(rows)