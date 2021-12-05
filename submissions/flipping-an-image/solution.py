# https://leetcode.com/problems/flipping-an-image

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        R, C = len(A), len(A[0])
        for r in range(R):
            for c in range(int(C/2)):
                A[r][c], A[r][C - 1 - c] = A[r][C - 1 - c], A[r][c]
        for r in range(R):
            for c in range(C):
                if A[r][c] == 0:
                    A[r][c] = 1
                else:
                    A[r][c] = 0
        return A
        