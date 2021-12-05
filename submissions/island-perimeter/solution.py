# https://leetcode.com/problems/island-perimeter

class Solution:
    def islandPerimeter(self, grid):
        R, C = len(grid), len(grid[0])
        perimeter = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    continue
                for y, x in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                    if y < 0 or R <= y or x < 0 or C <= x:
                        perimeter += 1
                    elif grid[y][x] == 0:
                        perimeter += 1
        return perimeter
                    


                
        