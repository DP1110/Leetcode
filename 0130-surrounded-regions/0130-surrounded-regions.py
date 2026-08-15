class Solution(object):
    def solve(self, board):
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        
        # Helper to mark safe 'O's from boundary
        def mark(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != 'O':
                return
            board[r][c] = 'S'  # Safe
            mark(r+1, c)
            mark(r-1, c)
            mark(r, c+1)
            mark(r, c-1)
        
        # Mark all 'O's connected to boundary
        for i in range(m):
            if board[i][0] == 'O':
                mark(i, 0)
            if board[i][n-1] == 'O':
                mark(i, n-1)
        for j in range(n):
            if board[0][j] == 'O':
                mark(0, j)
            if board[m-1][j] == 'O':
                mark(m-1, j)
        
        # Flip
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'