# https://leetcode.com/problems/edit-distance

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1 = ' ' + word1
        word2 = ' ' + word2
        R, C = len(word1), len(word2)
        dp = [[float('inf') for _ in range(C)] for __ in range(R)]
        for c in range(C):
            dp[0][c] = c
        for r in range(R):
            dp[r][0] = r
        
        for c in range(1, C):
            for r in range(1, R):
                if word1[r] == word2[c]:
                    dp[r][c] = min(dp[r-1][c-1], dp[r][c])
                dp[r][c] = min(dp[r][c], dp[r-1][c] + 1, dp[r][c-1] + 1, dp[r-1][c-1] + 1)
        return dp[-1][-1]