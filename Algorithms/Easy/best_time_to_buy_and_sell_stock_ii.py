# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices):
        sell, buy, hold = [0] * len(prices), [0] * len(prices), [0] * len(prices)
        buy[0] = -prices[0]
        ans = 0
        for i in range(1, len(prices)):
            if i == 1:
                hold[i] = buy[i-1]
                sell[i] = max(buy[i-1] + prices[i], sell[i-1])
            else:
                hold[i] = max(buy[i-1], hold[i-1])
                sell[i] = max(buy[i-1] + prices[i], hold[i-1] + prices[i], sell[i-1])
            buy[i] = sell[i-1] - prices[i]
            ans = max(hold[i], sell[i], buy[i])
        return ans
