# https://leetcode.com/problems/number-of-islands/

from collections import deque
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
            
        Y, X = len(grid), len(grid[0])
        def bfs(y, x):
            q = deque([(y, x)])
            dy = [0, 0, 1, -1]
            dx = [1, -1, 0, 0]
            while q:
                y_1, x_1 = q.popleft()
                for i in range(4):
                    y_2 = y_1 + dy[i]
                    x_2 = x_1 + dx[i]
                    if 0<=y_2 and y_2<Y and 0<=x_2 and x_2<X and grid[y_2][x_2]=="1":
                        q.append((y_2, x_2))
                        grid[y_2][x_2] = "0"

        
        res = 0
        for y in range(Y):
            for x in range(X):
                if grid[y][x]=="1":
                    bfs(y, x)
                    res += 1
        return res
