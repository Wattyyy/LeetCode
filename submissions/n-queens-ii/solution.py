# https://leetcode.com/problems/n-queens-ii

from collections import Counter


class Solution:
    def __init__(self):
        self.vertical = set()
        self.diagonal = Counter()
        self.ans = 0

    def add_diag(self, row, col, n):
        # lower left
        r, c = row + 1, col - 1
        while r < n and 0 <= c:
            self.diagonal[(r, c)] += 1
            r += 1
            c -= 1
        # lower right
        r, c = row + 1, col + 1
        while r < n and c < n:
            self.diagonal[(r, c)] += 1
            r += 1
            c += 1

    def subtract_diag(self, row, col, n):
        # lower left
        r, c = row + 1, col - 1
        while r < n and 0 <= c:
            self.diagonal[(r, c)] -= 1
            r += 1
            c -= 1
        # lower right
        r, c = row + 1, col + 1
        while r < n and c < n:
            self.diagonal[(r, c)] -= 1
            r += 1
            c += 1

    def recursion(self, row, n):
        if row == n:
            self.ans += 1
            return
        for col in range(n):
            if (col not in self.vertical) and (self.diagonal[(row, col)] == 0):
                self.vertical.add(col)
                self.add_diag(row, col, n)
                self.recursion(row + 1, n)
                self.vertical.remove(col)
                self.subtract_diag(row, col, n)

    def totalNQueens(self, n: int) -> int:
        self.recursion(0, n)
        return self.ans
