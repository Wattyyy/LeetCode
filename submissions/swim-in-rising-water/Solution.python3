// https://leetcode.com/problems/swim-in-rising-water

from collections import deque
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        min_val = max(grid[0][0], grid[-1][-1])
        for v in range(min_val, N * N):
            visited = {(0, 0)}
            queue = deque([(0, 0)])
            while queue:
                y, x = queue.popleft()
                if y == N - 1 and x == N - 1:
                    return v
                nexts = [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]
                for ny, nx in nexts:
                    if 0 <= ny < N and 0 <= nx < N and (ny, nx) not in visited and grid[ny][nx] <= v:
                        queue.append((ny, nx))
                        visited.add((ny, nx))
            
