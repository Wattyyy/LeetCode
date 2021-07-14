// https://leetcode.com/problems/minimum-path-sum

class Solution:
    def minPathSum(self, grid):
        R, C = len(grid), len(grid[0])
        dp = [[0 for _ in range(C)] for __ in range(R)]
        dp[0][0] = grid[0][0]
        for c in range(1, C):
            dp[0][c] = dp[0][c-1] + grid[0][c]
        for r in range(1, R):
            dp[r][0] = dp[r-1][0] + grid[r][0]
        
        print(dp)
        for r in range(1, R):
            for c in range(1, C):
                dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1])
        return dp[-1][-1]
        
            
        
                
        