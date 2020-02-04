# https://leetcode.com/problems/two-city-scheduling/

# step1: allocate 2N people to city A
# step2: move N people to B greedily 

class Solution(object):
    def twoCitySchedCost(self, costs):
        length = len(costs)
        switch_cost = []
        total_cost = 0
        for i in range(length):
            a, b = costs[i]
            switch_cost.append(b-a)
            total_cost += a
        switch_cost = sorted(switch_cost)
        for i in range(length//2):
            total_cost += switch_cost[i]
        return total_cost
