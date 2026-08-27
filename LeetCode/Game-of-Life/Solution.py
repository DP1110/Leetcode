1class Solution(object):
2    def gameOfLife(self, board):
3        m, n = len(board), len(board[0])
4
5        def live_neighbors(r, c):
6            cnt = 0
7            for dr in (-1, 0, 1):
8                for dc in (-1, 0, 1):
9                    if dr == 0 and dc == 0:
10                        continue
11                    nr, nc = r + dr, c + dc
12                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] in (1, 2):
13                        cnt += 1
14            return cnt
15
16        for r in range(m):
17            for c in range(n):
18                live = live_neighbors(r, c)
19                if board[r][c] == 1 and (live < 2 or live > 3):
20                    board[r][c] = 2  # live -> dead
21                elif board[r][c] == 0 and live == 3:
22                    board[r][c] = 3  # dead -> live
23
24        for r in range(m):
25            for c in range(n):
26                board[r][c] %= 2