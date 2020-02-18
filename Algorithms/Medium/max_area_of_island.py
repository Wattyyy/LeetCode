# https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid):
        if not grid:
            return 0
        R, C = len(grid), len(grid[0])
        self.area = 0
        def dfs(y, x):
            grid[y][x] = 0
            self.area += 1
            for ny, nx in [[y+1, x], [y-1, x], [y, x+1], [y, x-1]]:
                if 0 <= ny and ny < R and 0 <= nx and nx < C and grid[ny][nx] == 1:
                    dfs(ny, nx)
                    
        ans = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] != 1:
                    continue
                self.area = 0
                dfs(r, c)
                ans = max(ans, self.area)
        return ans
                    
        

