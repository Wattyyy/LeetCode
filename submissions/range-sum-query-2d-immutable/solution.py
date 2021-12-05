# https://leetcode.com/problems/range-sum-query-2d-immutable

from typing import List
from itertools import accumulate


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.R = len(matrix)
        self.C = len(matrix[0])
        self.sum_matrix = []
        for r in range(self.R):
            self.sum_matrix.append(list(accumulate(matrix[r])))

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for r in range(row1, row2 + 1):
            if col1 == 0:
                res += self.sum_matrix[r][col2]
            else:
                res += self.sum_matrix[r][col2] - self.sum_matrix[r][col1 - 1]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
