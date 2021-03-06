# https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        R, C = len(matrix), len(matrix[0])
        # avoid all zero case
        no_one = True
        length = 1
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == "1":
                    no_one = False
                if r == 0 or c == 0:
                    matrix[r][c] = int(matrix[r][c])
                else:
                    if (matrix[r][c] == "1") and (0 < matrix[r-1][c-1]) and (0 < matrix[r-1][c]) and (0 < matrix[r][c-1]):
                        min_val = min(matrix[r-1][c-1], matrix[r-1][c], matrix[r][c-1])
                        matrix[r][c] = min_val + 1
                        length = max(length, min_val + 1)
                    else:
                        matrix[r][c] = int(matrix[r][c])            
        if no_one:
            return 0
        else:
            return length*length
