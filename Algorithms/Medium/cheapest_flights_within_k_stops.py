# https://leetcode.com/problems/cheapest-flights-within-k-stops/

from collections import defaultdict
import heapq

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        # cost, step, sourse
        pq = [(0, K+1, src)]
        while pq:
            cost, step, cur_v = heapq.heappop(pq)
            if cur_v == dst:
                return cost
            if step > 0:
                for next_v, weight in graph[cur_v]:
                    newcost = cost + weight
                    heapq.heappush(pq, (newcost, step-1, next_v))
        return -1
