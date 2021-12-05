# https://leetcode.com/problems/max-increase-to-keep-city-skyline

class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        if not grid:
            return 0
        R, C = len(grid), len(grid[0])
        r_max, c_max = [0] * R, [0] * C
        for c in range(C):
            c_max[c] = max(grid[r][c] for r in range(R))
        for r in range(R):
            r_max[r] = max(grid[r][c] for c in range(C))

        ans = 0
        for r in range(R):
            for c in range(C):
                ans += min(r_max[r], c_max[c]) - grid[r][c]
        
        return ans