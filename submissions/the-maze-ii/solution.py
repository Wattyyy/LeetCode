# https://leetcode.com/problems/the-maze-ii

from collections import defaultdict, deque
from bisect import bisect_left
import sys


class Solution:
    def shortestDistance(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> int:
        INF = sys.maxsize
        row_walls, col_walls = defaultdict(list), defaultdict(list)
        R, C = len(maze), len(maze[0])
        dist_list = [[INF for _ in range(C)] for __ in range(R)]
        for r in range(R):
            for c in range(C):
                if c == 0:
                    row_walls[r].append(-1)
                if maze[r][c] == 1:
                    row_walls[r].append(c)
                if c == C - 1:
                    row_walls[r].append(C)

        for c in range(C):
            for r in range(R):
                if r == 0:
                    col_walls[c].append(-1)
                if maze[r][c] == 1:
                    col_walls[c].append(r)
                if r == R - 1:
                    col_walls[c].append(R)

        dy, dx = destination[0], destination[1]
        sy, sx = start[0], start[1]
        dist_list[sy][sx] = 0
        queue = deque([[sy, sx]])

        while queue:
            y, x = queue.popleft()

            idx = bisect_left(row_walls[y], x)
            # move right
            next_x = row_walls[y][idx] - 1
            if abs(next_x - x) + dist_list[y][x] < dist_list[y][next_x]:
                dist_list[y][next_x] = abs(next_x - x) + dist_list[y][x]
                queue.append([y, next_x])
            # move left
            next_x = row_walls[y][idx - 1] + 1
            if abs(next_x - x) + dist_list[y][x] < dist_list[y][next_x]:
                dist_list[y][next_x] = abs(next_x - x) + dist_list[y][x]
                queue.append([y, next_x])

            idx = bisect_left(col_walls[x], y)
            # move up
            next_y = col_walls[x][idx - 1] + 1
            if abs(next_y - y) + dist_list[y][x] < dist_list[next_y][x]:
                dist_list[next_y][x] = abs(next_y - y) + dist_list[y][x]
                queue.append([next_y, x])
            # move down
            next_y = col_walls[x][idx] - 1
            if abs(next_y - y) + dist_list[y][x] < dist_list[next_y][x]:
                dist_list[next_y][x] = abs(next_y - y) + dist_list[y][x]
                queue.append([next_y, x])

        if dist_list[dy][dx] == INF:
            return -1
        return dist_list[dy][dx]
