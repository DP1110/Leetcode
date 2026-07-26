class Solution(object):
    def convert(self, s, numRows):
        # Edge case: no zigzag possible
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create a list of strings, one per row
        rows = [''] * numRows
        current_row = 0
        direction = 1  # 1 = going down, -1 = going up
        
        for char in s:
            rows[current_row] += char
            
            # Flip direction at the boundaries
            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1
            
            current_row += direction
        
        # Concatenate all rows
        return ''.join(rows)