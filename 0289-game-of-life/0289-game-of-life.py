class Solution(object):
    def gameOfLife(self, board):
        m, n = len(board), len(board[0])

        def live_neighbors(r, c):
            cnt = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] in (1, 2):
                        cnt += 1
            return cnt

        for r in range(m):
            for c in range(n):
                live = live_neighbors(r, c)
                if board[r][c] == 1 and (live < 2 or live > 3):
                    board[r][c] = 2  # live -> dead
                elif board[r][c] == 0 and live == 3:
                    board[r][c] = 3  # dead -> live

        for r in range(m):
            for c in range(n):
                board[r][c] %= 2