class Solution:
    def isValidSudoku(self, board):
        seen = set()
        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if v != '.':
                    if (v, i) in seen or (j, v) in seen or (i//3, j//3, v) in seen:
                        return False
                    seen.add((v, i))
                    seen.add((j, v))
                    seen.add((i//3, j//3, v))
        return True