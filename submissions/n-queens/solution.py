# https://leetcode.com/problems/n-queens

from typing import List
from collections import Counter


class Solution:
    def __init__(self):
        self.ans = []
        self.col_visited = set()
        self.diag_visited = Counter()

    def diag_add(self, row, col, n):
        # lower left
        r, c = row + 1, col - 1
        while r < n and 0 <= c:
            self.diag_visited[(r, c)] += 1
            r += 1
            c -= 1
        # lower right
        r, c = row + 1, col + 1
        while r < n and c < n:
            self.diag_visited[(r, c)] += 1
            r += 1
            c += 1

    def diag_remove(self, row, col, n):
        # lower left
        r, c = row + 1, col - 1
        while r < n and 0 <= c:
            self.diag_visited[(r, c)] -= 1
            r += 1
            c -= 1
        # lower right
        r, c = row + 1, col + 1
        while r < n and c < n:
            self.diag_visited[(r, c)] -= 1
            r += 1
            c += 1

    def backtrack(self, ls, row, n):
        if row == n:
            res = []
            for row in ls:
                string = "".join(row)
                res.append(string)
            self.ans.append(res[:])
            return

        for col in range(n):
            if (col not in self.col_visited) and (self.diag_visited[(row, col)] == 0):
                self.col_visited.add(col)
                self.diag_add(row, col, n)
                ls[row][col] = "Q"
                self.backtrack(ls, row + 1, n)
                self.col_visited.remove(col)
                self.diag_remove(row, col, n)
                ls[row][col] = "."

    def solveNQueens(self, n: int) -> List[List[str]]:
        ls_init = [["." for _ in range(n)] for __ in range(n)]
        self.backtrack(ls_init, 0, n)
        return self.ans
