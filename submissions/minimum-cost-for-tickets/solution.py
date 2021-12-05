# https://leetcode.com/problems/minimum-cost-for-tickets

import sys
class Solution:
    def mincostTickets(self, days, costs):
        INF = sys.maxsize        
        last_d = days[-1]
        dp = [INF] * (last_d + 31)
        dp[0] = 0
        days_set = set(days)

        for d in range(1, last_d + 31):
            if d in days_set:
                # 1 days
                dp[d] = min(dp[d], dp[d-1] + costs[0])
                # 7 days
                for j in range(1, 8):
                    dp[d-1+j] = min(dp[d-1+j], dp[d-1] + costs[1])
                # 30 days
                for j in range(1, 31):
                    dp[d-1+j] = min(dp[d-1+j], dp[d-1] + costs[2])
            else:
                dp[d] = min(dp[d], dp[d-1])
            
        ans = INF
        for i in range(last_d, last_d + 31):
            ans = min(dp[i], ans)
        return ans

