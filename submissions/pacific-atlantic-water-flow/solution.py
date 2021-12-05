# https://leetcode.com/problems/pacific-atlantic-water-flow

from collections import deque


class Solution:
    def pacificAtlantic(self, matrix):
        if not matrix or len(matrix) == 0:
            return []
        pacific_queue, atlantic_queue = deque([]), deque([])
        pacific_set, atlantic_set = set(), set()
        R, C = len(matrix), len(matrix[0])
        for r in range(R):
            for c in range(C):
                if r == 0 or c == 0:
                    pacific_queue.append((r, c))
                    pacific_set.add((r, c))
                if r == R - 1 or c == C - 1:
                    atlantic_queue.append((r, c))
                    atlantic_set.add((r, c))

        while pacific_queue:
            r, c = pacific_queue.popleft()
            nexts = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            for nr, nc in nexts:
                if (
                    (0 <= nr < R)
                    and (0 <= nc < C)
                    and (matrix[r][c] <= matrix[nr][nc])
                    and ((nr, nc) not in pacific_set)
                ):
                    pacific_set.add((nr, nc))
                    pacific_queue.append((nr, nc))

        while atlantic_queue:
            r, c = atlantic_queue.popleft()
            nexts = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            for nr, nc in nexts:
                if (
                    (0 <= nr < R)
                    and (0 <= nc < C)
                    and (matrix[r][c] <= matrix[nr][nc])
                    and ((nr, nc) not in atlantic_set)
                ):
                    atlantic_set.add((nr, nc))
                    atlantic_queue.append((nr, nc))

        ret = pacific_set.intersection(atlantic_set)
        return list(ret)
