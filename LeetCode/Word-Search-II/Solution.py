1class Solution(object):
2    def findWords(self, board, words):
3        trie = {}
4        for word in words:
5            node = trie
6            for ch in word:
7                node = node.setdefault(ch, {})
8            node['#'] = word
9
10        rows, cols = len(board), len(board[0])
11        res = []
12
13        def dfs(r, c, node):
14            ch = board[r][c]
15            if ch not in node:
16                return
17            nxt = node[ch]
18            if '#' in nxt:
19                res.append(nxt['#'])
20                del nxt['#']
21
22            board[r][c] = '*'
23            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
24                nr, nc = r+dr, c+dc
25                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '*':
26                    dfs(nr, nc, nxt)
27            board[r][c] = ch
28
29            if not nxt:
30                del node[ch]
31
32        for r in range(rows):
33            for c in range(cols):
34                dfs(r, c, trie)
35
36        return res