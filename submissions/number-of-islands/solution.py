# https://leetcode.com/problems/number-of-islands


class Solution:
    def __init__(self):
        self.ans = 0

    def dfs(self, y, x, grid):
        grid[y][x] = "0"
        for ny, nx in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
            if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] == "1":
                self.dfs(ny, nx, grid)

    def numIslands(self, grid):
        if not grid:
            return 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    self.dfs(y, x, grid)
                    self.ans += 1
        return self.ans
