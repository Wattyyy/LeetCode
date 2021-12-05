# https://leetcode.com/problems/surrounded-regions


class Solution:
    def __init__(self):
        self.flag = False

    def dfs(self, y, x, board):
        board[y][x] = "△"
        R, C = len(board), len(board[0])
        if y == 0 or y == R - 1 or x == 0 or x == C - 1:
            self.flag = True
        for ny, nx in [[y + 1, x], [y - 1, x], [y, x + 1], [y, x - 1]]:
            if 0 <= ny < R and 0 <= nx < C and board[ny][nx] == "O":
                self.dfs(ny, nx, board)

    def dfs2(self, y, x, board):
        if self.flag:
            board[y][x] = "O"
        else:
            board[y][x] = "X"
        R, C = len(board), len(board[0])
        for ny, nx in [[y + 1, x], [y - 1, x], [y, x + 1], [y, x - 1]]:
            if 0 <= ny < R and 0 <= nx < C and board[ny][nx] == "△":
                self.dfs2(ny, nx, board)

    def solve(self, board):
        if not board:
            return
        R, C = len(board), len(board[0])
        for r in range(R):
            for c in range(C):
                if board[r][c] == "X":
                    continue
                self.dfs(r, c, board)
                self.dfs2(r, c, board)
                self.flag = False
        return
