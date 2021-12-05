# https://leetcode.com/problems/the-maze

from collections import defaultdict
from bisect import bisect_left


class Solution:
    def dfs(self, y, x, maze, visited):
        visited[y][x] = 1

        # move right
        idx = bisect_left(self.row_walls[y], x)
        next_x = self.row_walls[y][idx] - 1
        if visited[y][next_x] == 0:
            self.dfs(y, next_x, maze, visited)

        # move left
        idx = bisect_left(self.row_walls[y], x)
        next_x = self.row_walls[y][idx - 1] + 1
        if visited[y][next_x] == 0:
            self.dfs(y, next_x, maze, visited)

        # move up
        idx = bisect_left(self.col_walls[x], y)
        next_y = self.col_walls[x][idx - 1] + 1
        if visited[next_y][x] == 0:
            self.dfs(next_y, x, maze, visited)

        # move down
        idx = bisect_left(self.col_walls[x], y)
        next_y = self.col_walls[x][idx] - 1
        if visited[next_y][x] == 0:
            self.dfs(next_y, x, maze, visited)

    def hasPath(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> bool:
        row_walls, col_walls = defaultdict(list), defaultdict(list)
        R, C = len(maze), len(maze[0])
        visited = [[0 for _ in range(C)] for __ in range(R)]
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

        self.row_walls, self.col_walls = row_walls, col_walls
        self.dfs(start[0], start[1], maze, visited)

        if visited[destination[0]][destination[1]]:
            return True
        else:
            return False
