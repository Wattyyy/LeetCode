// https://leetcode.com/problems/cyclically-rotating-a-grid

class Solution:
    def rotate(self, grid,  i, k):
        R, C = len(grid), len(grid[0])
        ls = []
        for r in range(i, R - i - 1):
            ls.append(grid[r][i])
        for c in range(i, C - i - 1):
            ls.append(grid[R-i-1][c])
        for r in reversed(range(i + 1, R - i)):
            ls.append(grid[r][C - i - 1])
        for c in reversed(range(i + 1, C - i)):
            ls.append(grid[i][c])
        
        L = len(ls)
        new = [0] * L
        for x in range(L):
            idx = (x + k) % L
            new[idx] += ls[x]
        idx = 0
        for r in range(i, R - i - 1):
            grid[r][i] = new[idx]
            idx += 1
        for c in range(i, C - i - 1):
            grid[R-i-1][c] = new[idx]
            idx += 1
        for r in reversed(range(i + 1, R - i)):
            grid[r][C - i - 1] = new[idx]
            idx += 1
        for c in reversed(range(i + 1, C - i)):
            grid[i][c] = new[idx]
            idx += 1
       
        
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        R, C = len(grid), len(grid[0])
        for i in range(min(R, C) // 2):
            self.rotate(grid, i, k)
        return grid
            
            
        
        