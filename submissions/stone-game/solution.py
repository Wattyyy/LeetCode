// https://leetcode.com/problems/stone-game

from typing import List
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)
        dp = [[0 for _ in range(N)] for __ in range(N)]
        for i in reversed(range(N)):
            for j in range(i, N):
                if i == j:
                    dp[i][j] = piles[i]
                else:
                    dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
        return 0 < dp[0][-1]
        