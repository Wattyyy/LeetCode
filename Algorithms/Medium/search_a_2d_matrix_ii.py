# https://leetcode.com/problems/search-a-2d-matrix-ii/

from bisect import bisect_right
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or matrix == [[]]:
            return False        
        R, C = len(matrix), len(matrix[0])
        for r in range(R):
            idx = bisect_right(matrix[r], target)
            if matrix[r][idx-1] == target:
                return True
        return False
        
