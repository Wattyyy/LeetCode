# https://leetcode.com/problems/sudoku-solver

from collections import defaultdict
from typing import List

class Solution:
    def __init__(self) -> None:
        self.cell = defaultdict(set)
        self.row = defaultdict(set)
        self.col = defaultdict(set)
        self.flag = False
    
    def backtrack(self, board, idx):
        if len(self.empties) == idx:
            self.flag = True
            return
        r, c = self.empties[idx]
        for d in range(1, 10):
            if self.flag:
                return
            if (d in self.cell[(r // 3, c // 3)]) or (d in self.row[r]) or (d in self.col[c]):
                continue
            else:
                self.cell[(r // 3, c // 3)].add(d)
                self.row[r].add(d)
                self.col[c].add(d)
                board[r][c] = str(d)
                self.backtrack(board, idx+1)
                self.cell[(r // 3, c // 3)].remove(d)
                self.row[r].remove(d)
                self.col[c].remove(d)
        
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.empties = []
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    self.empties.append((r, c))
                else:
                    d = int(board[r][c])
                    self.cell[(r // 3, c // 3)].add(d)
                    self.row[r].add(d)
                    self.col[c].add(d)
        self.backtrack(board, 0)
        return
        
        