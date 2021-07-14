// https://leetcode.com/problems/knight-probability-in-chessboard

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[[0 for _ in range(k+1)] for __ in range(n)] for ___ in range(n)]
        for r in range(n):
            for c in range(n):
                dp[r][c][0] = 1
        
        for mv in range(1, k + 1):
            for r in range(n):
                for c in range(n):
                    nexts = [(r-2, c+1), (r-1, c+2), (r+1, c+2), (r+2, c+1),
                             (r+2, c-1), (r+1, c-2), (r-1, c-2), (r-2, c-1)]
                    for nr, nc in nexts:
                        if 0 <= nr < n and 0 <= nc < n:
                            dp[r][c][mv] += dp[nr][nc][mv-1]
        
        return dp[row][column][k] / (pow(8, k))
            
            