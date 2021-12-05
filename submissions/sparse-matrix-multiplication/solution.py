# https://leetcode.com/problems/sparse-matrix-multiplication

class Solution:
    def multiply(self, A, B):
        if not A or not B:
            return [[]]
        R, K, C = len(A), len(A[0]),len(B[0])
        res = [[0 for _ in range(C)] for __ in range(R)]
        for r in range(R):
            for c in range(C):
                val = 0
                for k in range(K):
                    val += A[r][k] * B[k][c]
                res[r][c] = val
        return res