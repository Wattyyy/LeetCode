# https://leetcode.com/problems/range-sum-query-2d-immutable/

import numpy as np
class NumMatrix:
    
    def __init__(self, matrix):
        if (matrix is None) or (not matrix):
            return
        m = np.array(matrix)
        if len(m.shape) > 2:
            m = m.reshape(m.shape[-2], m.shape[-1])
            self.mat = m
        else:
            self.mat = matrix
        R, C = len(self.mat), len(self.mat[0])
        for r in range(R):
            for c in range(1, C):
                self.mat[r][c] += self.mat[r][c-1]
        for c in range(C):
            for r in range(1, R):
                self.mat[r][c] += self.mat[r-1][c]

                
    def sumRegion(self, row1, col1, row2, col2):
        if row1 == col1 == 0:
            return self.mat[row2][col2]
        elif row1 == 0 and col1 != 0:
            return self.mat[row2][col2] - self.mat[row2][col1-1]
        elif row1 != 0 and col1 == 0:
            return self.mat[row2][col2] - self.mat[row1-1][col2]
        else:
            return self.mat[row2][col2] + self.mat[row1-1][col1-1] - self.mat[row2][col1-1] - self.mat[row1-1][col2]
               
