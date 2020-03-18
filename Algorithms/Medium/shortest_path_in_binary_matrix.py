# https://leetcode.com/problems/shortest-path-in-binary-matrix/

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        if grid[0][0] == 1:
            return -1
        R, C = len(grid), len(grid[0])
        path = [[float('inf') for _ in range(C)] for __ in range(R)]
        path[0][0] = 1
        queue = [(0, 0)]
        nx = [(1, 0), (-1, 0), (0, 1), (0, -1),
                 (1, 1), (1, -1), (-1, 1), (-1, -1)]
        while queue:
            y, x = queue.pop(0)
            for vy, vx in nx:
                if 0 <= y + vy and y + vy < R and 0 <= x + vx and x + vx < C:
                    if (grid[y + vy][x + vx] == 0) and (path[y][x] + 1 < path[y + vy][x + vx]):
                        path[y + vy][x + vx] = path[y][x] + 1
                        queue.append((y + vy, x + vx))
        
        if path[-1][-1] == float('inf'):
            return -1
        else:
            return path[-1][-1]
            
