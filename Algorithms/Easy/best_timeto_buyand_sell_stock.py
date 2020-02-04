# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices):
        N = len(prices)
        if (N == 0) or (N == 1):
            return 0
        ans = prices[1] - prices[0]
        min_val = min(prices[1], prices[0])
        for i in range(2, N):
            val = prices[i] - min_val
            if val > ans:
                ans = val
            if min_val > prices[i]:
                min_val = prices[i]    
        if ans < 0:
            return 0
        return ans
