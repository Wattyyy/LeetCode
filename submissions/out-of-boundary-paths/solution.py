# https://leetcode.com/problems/out-of-boundary-paths


class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        # dp[row][col][move] = paths
        M = 7 + 10 ** 9
        R, C = m, n
        dp = [[[0 for _ in range(maxMove + 1)] for __ in range(C)] for ___ in range(R)]
        for move in range(1, maxMove + 1):
            for r in range(R):
                for c in range(C):
                    nexts = [(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)]
                    for nr, nc in nexts:
                        if 0 <= nr < R and 0 <= nc < C:
                            dp[r][c][move] += dp[nr][nc][move - 1]
                            dp[r][c][move] %= M
                        else:
                            dp[r][c][move] += 1
                            dp[r][c][move] %= M

        return dp[startRow][startColumn][maxMove] % M
