# https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid):
        if not grid or grid == [[]]:
            return 0
        R, C = len(grid), len(grid[0])
        new = [[float('inf') for _ in range(C)] for __ in range(R)]
        new[0][0] = grid[0][0]
        queue = [(0, 0)]
        while queue:
            y, x = queue.pop(0) 
            if y + 1 < R and (new[y][x] + grid[y + 1][x] < new[y + 1][x]):
                new[y+1][x] = new[y][x] + grid[y+1][x]
                queue.append((y + 1, x))
            if x + 1 < C and (new[y][x] + grid[y][x + 1] < new[y][x + 1]):
                new[y][x + 1] = new[y][x] + grid[y][x + 1]
                queue.append((y, x + 1))    
        return new[-1][-1]
            

        
