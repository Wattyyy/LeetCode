// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee

class Solution:
    def maxProfit(self, prices, fee):
        if not prices:
            return 0
        N = len(prices)
        # sell
        s0 = [0 for _ in range(N)]
        # buy
        s1 = [0 for _ in range(N)]
        s0[0] = 0
        s1[0] = 0 - prices[0] - fee
        for i in range(1, N):
            s0[i] = max(s0[i-1], prices[i] + s1[i-1])
            s1[i] = max(s1[i-1], s0[i-1] - prices[i] - fee)
        return max(s0[N-1], s1[N-1])