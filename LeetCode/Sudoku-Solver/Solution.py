1class Solution:
2    def solveSudoku(self, board):
3        rows = [set() for _ in range(9)]
4        cols = [set() for _ in range(9)]
5        boxes = [set() for _ in range(9)]
6        empty = []
7        
8        # Initialize: record existing numbers
9        for i in range(9):
10            for j in range(9):
11                if board[i][j] == '.':
12                    empty.append((i, j))
13                else:
14                    val = board[i][j]
15                    rows[i].add(val)
16                    cols[j].add(val)
17                    boxes[(i // 3) * 3 + (j // 3)].add(val)
18        
19        def backtrack(idx):
20            if idx == len(empty):
21                return True
22            
23            i, j = empty[idx]
24            box_idx = (i // 3) * 3 + (j // 3)
25            
26            for num in map(str, range(1, 10)):
27                if num not in rows[i] and num not in cols[j] and num not in boxes[box_idx]:
28                    # Place
29                    board[i][j] = num
30                    rows[i].add(num)
31                    cols[j].add(num)
32                    boxes[box_idx].add(num)
33                    
34                    if backtrack(idx + 1):
35                        return True
36                    
37                    # Backtrack
38                    board[i][j] = '.'
39                    rows[i].remove(num)
40                    cols[j].remove(num)
41                    boxes[box_idx].remove(num)
42            
43            return False
44        
45        backtrack(0)