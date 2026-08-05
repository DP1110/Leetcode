1class Solution:
2    def isValidSudoku(self, board):
3        seen = set()
4        for i in range(9):
5            for j in range(9):
6                v = board[i][j]
7                if v != '.':
8                    if (v, i) in seen or (j, v) in seen or (i//3, j//3, v) in seen:
9                        return False
10                    seen.add((v, i))
11                    seen.add((j, v))
12                    seen.add((i//3, j//3, v))
13        return True