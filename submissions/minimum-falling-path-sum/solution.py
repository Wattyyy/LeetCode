# https://leetcode.com/problems/minimum-falling-path-sum


class Solution:
    def minFallingPathSum(self, A):
        if not A:
            return 0
        R, C = len(A), len(A[0])
        dp = [[0 for _ in range(C)] for __ in range(R)]
        for c in range(C):
            dp[0][c] = A[0][c]

        for r in range(1, R):
            for c in range(C):
                if c == 0:
                    dp[r][c] = min(dp[r - 1][c] + A[r][c], dp[r - 1][c + 1] + A[r][c])
                elif c == C - 1:
                    dp[r][c] = min(dp[r - 1][c - 1] + A[r][c], dp[r - 1][c] + A[r][c])
                else:
                    dp[r][c] = min(
                        dp[r - 1][c - 1] + A[r][c],
                        dp[r - 1][c] + A[r][c],
                        dp[r - 1][c + 1] + A[r][c],
                    )
        return min(dp[R - 1])
