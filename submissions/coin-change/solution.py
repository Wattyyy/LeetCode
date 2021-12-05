# https://leetcode.com/problems/coin-change

import sys


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = sys.maxsize
        dp = [MAX] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for val in coins:
                if 0 <= i - val:
                    dp[i] = min(dp[i - val] + 1, dp[i])

        if dp[-1] == MAX:
            return -1
        else:
            return dp[-1]
