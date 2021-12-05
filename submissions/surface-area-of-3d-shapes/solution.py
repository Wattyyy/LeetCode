# https://leetcode.com/problems/surface-area-of-3d-shapes


class Solution:
    def surfaceArea(self, grid):
        N = len(grid)
        ans = 0
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 0:
                    continue
                height = grid[i][j]
                ans += 2
                for h in range(1, height + 1):
                    adj = [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]
                    for a, b in adj:
                        if a < 0 or N <= a or b < 0 or N <= b:
                            ans += 1
                        else:
                            if h <= grid[a][b]:
                                ans += 0
                            else:
                                ans += 1
        return ans
