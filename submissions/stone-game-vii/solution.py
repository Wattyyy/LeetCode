# https://leetcode.com/problems/stone-game-vii

from itertools import accumulate
from typing import List


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        cum_sum = list(accumulate(stones))
        cum_sum = [0] + cum_sum
        N = len(stones)
        dp = [[0 for _ in range(N)] for __ in range(N)]
        for i in reversed(range(N)):
            for j in range(i, N):
                if i == j:
                    continue
                elif j - i == 1:
                    dp[i][j] = max(stones[i], stones[j])
                else:
                    dp[i][j] = max(
                        cum_sum[j + 1] - cum_sum[i + 1] - dp[i + 1][j],
                        cum_sum[j] - cum_sum[i] - dp[i][j - 1],
                    )

        return dp[0][-1]
