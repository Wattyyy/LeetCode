# https://leetcode.com/problems/uncrossed-lines


from collections import defaultdict


class Solution:
    def maxUncrossedLines(self, A, B):
        dp, m, n = defaultdict(int), len(A), len(B)
        for i in range(m):
            for j in range(n):
                dp[(i, j)] = max(
                    dp[(i - 1, j - 1)] + (A[i] == B[j]), dp[(i - 1, j)], dp[(i, j - 1)]
                )
        return dp[(m - 1, n - 1)]
