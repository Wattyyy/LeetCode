// https://leetcode.com/problems/leftmost-column-with-at-least-a-one

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#     def get(self, x: int, y: int) -> int:
#     def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        R, C = binaryMatrix.dimensions()
        ans = C
        for r in range(R):
            left, right = 0, C
            while left < right:
                mid = (left + right) // 2
                num = binaryMatrix.get(r, mid)
                if num == 1:
                    right = mid
                else:
                    left = mid+1
            ans = min(ans, left)
        if ans == C:
            return -1
        else:
            return ans

            


