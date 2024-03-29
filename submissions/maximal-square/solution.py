# https://leetcode.com/problems/maximal-square


class Solution:
    def maximalSquare(self, matrix):
        if matrix == [] or matrix == [[]]:
            return 0

        R, C = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(C)] for __ in range(R)]
        if matrix[0][0] == "1":
            dp[0][0] = 1

        for c in range(1, C):
            if matrix[0][c] == "1":
                dp[0][c] = 1

        for r in range(1, R):
            if matrix[r][0] == "1":
                dp[r][0] = 1

        no_one = True
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == "1":
                    no_one = False
        if no_one:
            return 0

        res = 1
        for r in range(1, R):
            for c in range(1, C):
                if matrix[r][c] == "1":
                    dp[r][c] = min(dp[r - 1][c - 1], dp[r - 1][c], dp[r][c - 1]) + 1
                    res = max(dp[r][c], res)
        return res ** 2
