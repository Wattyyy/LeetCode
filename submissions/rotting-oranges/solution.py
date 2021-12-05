# https://leetcode.com/problems/rotting-oranges

from collections import deque
class Solution:
    def orangesRotting(self, grid):
        R, C = len(grid), len(grid[0])
        fresh_flag = False
        queue = deque([])
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh_flag = True

        if not queue and fresh_flag:
            return -1

        cnt = 0
        while queue:
            new_queue = deque([])
            for r, c in queue:
                nexts = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
                for ny, nx in nexts:
                    if (0 <= ny < R) and (0 <= nx < C) and (grid[ny][nx] == 1):
                        grid[ny][nx] = 2
                        new_queue.append((ny, nx))            
            if 0 < len(new_queue):
                cnt += 1
            queue = new_queue


        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    return -1
        return cnt

            
                    
        