# https://leetcode.com/problems/paint-house


class Solution:
    def minCost(self, costs):
        if not costs:
            return 0
        n = len(costs)
        dp0, dp1, dp2 = [0] * n, [0] * n, [0] * n
        dp0[0], dp1[0], dp2[0] = costs[0][0], costs[0][1], costs[0][2]
        for i in range(1, n):
            dp0[i] = min(dp1[i - 1], dp2[i - 1]) + costs[i][0]
            dp1[i] = min(dp0[i - 1], dp2[i - 1]) + costs[i][1]
            dp2[i] = min(dp0[i - 1], dp1[i - 1]) + costs[i][2]
        return min(dp0[-1], dp1[-1], dp2[-1])
