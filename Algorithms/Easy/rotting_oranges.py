# https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid):
        R, C = len(grid), len(grid[0])
        time_grid = [[float("inf") if grid[r][c]==1 else 0 for c in range(C)] for r in range(R)]
        for r in range(R):
            for c in range(C):
                if grid[r][c] != 2:
                    continue
                visited = set((r, c))
                queue = [(r, c)]
                while queue:
                    row, col = queue.pop(0)
                    time = time_grid[row][col]
                    vy = [1, -1, 0, 0]
                    vx = [0, 0, 1, -1]
                    for i in range(4):
                        y = row + vy[i]
                        x = col + vx[i]
                        if (0<=y and y<R) and (0<=x and x<C) and (grid[y][x]!=0) and ((y, x) not in visited):
                            queue.append((y, x))
                            time_grid[y][x] = min(time_grid[y][x], time+1)
                            print(time_grid[y][x])
                            visited.add((y, x))

        res = 0
        for r in range(R):
            for c in range(C):
                res = max(res, time_grid[r][c])
        if res == float("inf"):
            return -1
        else:
            return res
                        
                
                
        
