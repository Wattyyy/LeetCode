// https://leetcode.com/problems/count-square-submatrices-with-all-ones

class Solution:
    def countSquares(self, matrix):
        R, C = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(C)] for __ in range(R)]
        ans = 0
        for r in range(R):
            for c in range(C):
                if r == 0 or c == 0:
                    dp[r][c] = matrix[r][c]
                elif matrix[r][c] == 1:
                    dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
                ans += dp[r][c]
        return ans

                     