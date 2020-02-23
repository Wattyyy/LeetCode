# https://leetcode.com/problems/coin-change-2/

class Solution:
    def change(self, amount, coins):
        if amount < 1:
            return 1
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[-1]
        
        
