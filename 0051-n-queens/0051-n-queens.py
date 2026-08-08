class Solution:
    def solveNQueens(self, n):
        res, cols, d1, d2 = [], set(), set(), set()
        board = [["."]*n for _ in range(n)]
        def bt(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in cols or (r-c) in d1 or (r+c) in d2:
                    continue
                cols.add(c); d1.add(r-c); d2.add(r+c); board[r][c] = "Q"
                bt(r+1)
                cols.remove(c); d1.remove(r-c); d2.remove(r+c); board[r][c] = "."
        bt(0)
        return res