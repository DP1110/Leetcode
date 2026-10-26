class Solution:
    def countIslands(self, grid, k):
        R, C = len(grid), len(grid[0])
        count = 0

        for i in range(R):
            for j in range(C):
                if grid[i][j] > 0:
                    total = 0
                    stack = [(i, j)]
                    total += grid[i][j]
                    grid[i][j] = 0
                    while stack:
                        x, y = stack.pop()
                        for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                            if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] > 0:
                                total += grid[nx][ny]
                                grid[nx][ny] = 0
                                stack.append((nx, ny))
                    if total % k == 0:
                        count += 1
        return count