# https://leetcode.com/problems/rotate-image

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        if N % 2 == 1:
            end = 1 + N // 2
        else:
            end = N // 2
        for r in range(end):
            for c in range(r, N - 1 - r):
                cnt = c - r
                (
                    matrix[r][c],
                    matrix[c][N - 1 - r],
                    matrix[N - 1 - r][N - 1 - r - cnt],
                    matrix[N - 1 - cnt - r][r],
                ) = (
                    matrix[N - 1 - cnt - r][r],
                    matrix[r][c],
                    matrix[c][N - 1 - r],
                    matrix[N - 1 - r][N - 1 - r - cnt],
                )
                # print((r, c), (c, N-1-r), (N-1-r, N-1-cnt), (N-1-cnt, r))
        return
