1class Solution(object):
2    def exist(self, board, word):
3        rows, cols = len(board), len(board[0])
4
5        def dfs(r, c, i):
6            if i == len(word):
7                return True
8            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
9                return False
10
11            temp = board[r][c]
12            board[r][c] = '#'  # mark visit
13
14            found = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or
15                     dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
16
17            board[r][c] = temp  # unmark
18            return found
19
20        for r in range(rows):
21            for c in range(cols):
22                if dfs(r, c, 0):
23                    return True
24        return False