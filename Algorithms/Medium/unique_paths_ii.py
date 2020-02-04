# https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])
        dp = [[0 for _ in range(N)] for __ in range(M)]
        dp[0][0] = 1
        for m in range(M):
            for n in range(N):
                if m==0 and n==0:
                    continue
                if obstacleGrid[m][n]==1:
                    dp[m][n] = 0
                else:
                    if m==0:
                        dp[m][n] = dp[m][n-1]
                    elif n==0:
                        dp[m][n] = dp[m-1][n]
                    else:
                        dp[m][n] = dp[m-1][n] + dp[m][n-1]
        return dp[M-1][N-1]
