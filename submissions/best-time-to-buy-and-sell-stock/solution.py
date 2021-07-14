// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices):
        if not prices or len(prices)==1:
            return 0
        min_val = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] > min_val:
                ans = max(prices[i]-min_val, ans)
            min_val = min(prices[i], min_val)
        return ans
        
        