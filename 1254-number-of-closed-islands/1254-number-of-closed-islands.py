class Solution:
    def closedIsland(self, grid):
        R, C = len(grid), len(grid[0])

        def flood(r, c):
            stack = [(r, c)]
            grid[r][c] = 1
            while stack:
                x, y = stack.pop()
                for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                    if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        stack.append((nx, ny))

        # kill border land
        for i in range(R):
            for j in range(C):
                if (i in (0, R - 1) or j in (0, C - 1)) and grid[i][j] == 0:
                    flood(i, j)

        # count inner islands
        count = 0
        for i in range(1, R - 1):
            for j in range(1, C - 1):
                if grid[i][j] == 0:
                    count += 1
                    flood(i, j)
        return count