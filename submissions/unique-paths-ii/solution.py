# https://leetcode.com/problems/unique-paths-ii


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        R, C = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(C)] for __ in range(R)]
        if obstacleGrid[0][0] != 1:
            dp[0][0] = 1
        for r in range(R):
            for c in range(C):
                if (r == c == 0) or (obstacleGrid[r][c] == 1):
                    continue
                if 0 <= r - 1:
                    dp[r][c] += dp[r - 1][c]
                if 0 <= c - 1:
                    dp[r][c] += dp[r][c - 1]
        return dp[-1][-1]
