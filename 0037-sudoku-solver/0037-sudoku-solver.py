class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []
        
        # Initialize: record existing numbers
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    val = board[i][j]
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i // 3) * 3 + (j // 3)].add(val)
        
        def backtrack(idx):
            if idx == len(empty):
                return True
            
            i, j = empty[idx]
            box_idx = (i // 3) * 3 + (j // 3)
            
            for num in map(str, range(1, 10)):
                if num not in rows[i] and num not in cols[j] and num not in boxes[box_idx]:
                    # Place
                    board[i][j] = num
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box_idx].add(num)
                    
                    if backtrack(idx + 1):
                        return True
                    
                    # Backtrack
                    board[i][j] = '.'
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[box_idx].remove(num)
            
            return False
        
        backtrack(0)