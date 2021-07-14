// https://leetcode.com/problems/max-area-of-island

from typing import List

class Solution:
    def __init__(self) -> None:
        self.cnt = 0

    def helper(self, r: int, c: int, grid: List[List[int]]) -> int:
        grid[r][c] = 0
        self.cnt += 1
        R, C = len(grid), len(grid[0])
        for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                self.helper(nr, nc, grid)
        return

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        ans = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    self.helper(r, c, grid)
                    ans = max(ans, self.cnt)
                    self.cnt = 0
        return ans


                    

        
        