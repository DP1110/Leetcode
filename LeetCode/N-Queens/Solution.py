1class Solution:
2    def solveNQueens(self, n):
3        res, cols, d1, d2 = [], set(), set(), set()
4        board = [["."]*n for _ in range(n)]
5        def bt(r):
6            if r == n:
7                res.append(["".join(row) for row in board])
8                return
9            for c in range(n):
10                if c in cols or (r-c) in d1 or (r+c) in d2:
11                    continue
12                cols.add(c); d1.add(r-c); d2.add(r+c); board[r][c] = "Q"
13                bt(r+1)
14                cols.remove(c); d1.remove(r-c); d2.remove(r+c); board[r][c] = "."
15        bt(0)
16        return res