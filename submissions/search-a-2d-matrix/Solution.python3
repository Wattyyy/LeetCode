// https://leetcode.com/problems/search-a-2d-matrix

from bisect import bisect_right
class Solution:
    def searchMatrix(self, matrix, target):
        if matrix == [[]] or matrix == []:
            return False
        
        R, C = len(matrix), len(matrix[0])
        if R == 1:
            idx = bisect_right(matrix[0], target)
            if idx == 0:
                return False
            else:
                return (matrix[0][idx-1] == target)
        
        top, bottom = 0, R - 1
        while top < bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] == target:
                return True
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                if mid == R - 1:
                    bottom = R - 1
                    break
                elif target < matrix[mid+1][0]:
                    bottom = mid
                    break
                else:
                    top = mid + 1
        idx = bisect_right(matrix[bottom], target)
        if idx == 0:
            return False
        else:
            return (matrix[bottom][idx-1] == target)
        
        