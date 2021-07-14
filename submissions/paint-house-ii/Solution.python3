// https://leetcode.com/problems/paint-house-ii

class Solution:
    def minCostII(self, costs):
        if not costs:
            return 0
        INF = float("inf")
        N, K = len(costs), len(costs[0])
        dp = [[0 for _ in range(K)] for __ in range(N)]
        f_min = [INF, INF]
        s_min = [INF, INF]
        for k in range(K):
            dp[0][k] = costs[0][k]
            if costs[0][k] < f_min[0]:
                s_min[0], s_min[1] = f_min[0], f_min[1]
                f_min[0], f_min[1] = costs[0][k], k
            elif costs[0][k] < s_min[0]:
                s_min[0], s_min[1] = costs[0][k], k    
            
        for i in range(1, N):
            next_f_min = [INF, INF]
            next_s_min = [INF, INF]
            for k in range(K):
                if f_min[1] != k:
                    dp[i][k] = f_min[0] + costs[i][k]
                else:
                    dp[i][k] = s_min[0] + costs[i][k]
                
                if dp[i][k] < next_f_min[0]:
                    next_s_min[0], next_s_min[1] = next_f_min[0], next_f_min[1]
                    next_f_min[0], next_f_min[1] = dp[i][k], k                
                elif dp[i][k] < next_s_min[0]:
                    next_s_min[0], next_s_min[1] = dp[i][k], k   
                
            f_min, s_min = next_f_min, next_s_min
        
        return f_min[0]

        