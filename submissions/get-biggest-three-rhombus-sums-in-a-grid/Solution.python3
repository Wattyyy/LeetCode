// https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid

from typing import List

class Solution:
    def helper(self, r, c, i, grid):
        if i == 0:
            return grid[r][c]

        R, C = len(grid), len(grid[0])
        if r-i < 0 or R <= r+i or c-i < 0 or C <= c+i:
            return 0

        cand = set()
        for dr in range(i+1):
            dc = i - dr
            cand.add((r + dr, c + dc))
            cand.add((r - dr, c + dc))
            cand.add((r + dr, c - dc))
            cand.add((r - dr, c - dc))

        res = 0
        for nr, nc in cand:
            res += grid[nr][nc]
        return res


    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        R, C = len(grid), len(grid[0])
        sum_set = set()
        for r in range(R):
            for c in range(C):
                for i in range(min(R, C) // 2 + 1):
                    res = self.helper(r, c, i, grid)
                    if res == 0:
                        continue
                    else:
                        sum_set.add(res)
        
        sum_set = sorted(list(sum_set), reverse=True)
        if len(sum_set) == 1:
            return [sum_set[0]]
        elif len(sum_set) == 2:
            return sum_set[:2]
        else:
            return sum_set[:3]
        