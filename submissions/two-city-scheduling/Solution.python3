// https://leetcode.com/problems/two-city-scheduling

import heapq
class Solution:
    def twoCitySchedCost(self, costs):
        min_heap = []
        cost = 0
        for a, b in costs:
            cost += b
            heapq.heappush(min_heap, a - b)
        N = len(costs) // 2
        for _ in range(N):
            diff = heapq.heappop(min_heap)
            cost += diff
        return cost

        