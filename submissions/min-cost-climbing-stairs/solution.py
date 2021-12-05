# https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # avoid index error
        cost = [0] + cost + [0]
        length = len(cost)
        memo = {}
        memo[0], memo[1] = cost[0], cost[1]
        
        for i in range(2, length):
            memo[i] = min( memo[i-2]+cost[i], memo[i-1]+cost[i] )
            
        return memo[length-1]