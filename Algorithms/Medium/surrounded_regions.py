# https://leetcode.com/problems/surrounded-regions/

import sys
sys.setrecursionlimit(10 ** 6)

class Solution:
    def solve(self, board):
        if not board:
            return
        R, C = len(board), len(board[0])
        self.visited = set()
        self.no_surrounded = False
        def dfs(y, x):
            if y == 0 or y == R - 1 or x == 0 or x == C - 1:
                self.no_surrounded = True
            self.visited.add((y, x))
            nexts = [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
            for ny, nx in nexts:
                if ((ny, nx) not in self.visited) and (0 <= ny and ny < R and 0 <= nx and nx < C):
                    if board[ny][nx] == 'O':
                        dfs(ny, nx)

        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O':
                    dfs(r, c)
                    if self.no_surrounded:
                        for y, x in self.visited:
                            board[y][x] = 'N'
                    else:
                        for y, x in self.visited:
                            board[y][x] = 'X'
                    self.visited = set()
                    self.no_surrounded = False
        
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'N':
                    board[r][c] = 'O'
        
        
        
