# https://leetcode.com/problems/network-delay-time

import heapq
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times, N, K):

        graph = defaultdict(list)
        for u, v, w in times:
            graph[u - 1].append((v - 1, w))
        dist = [float("inf")] * N
        dist[K - 1] = 0
        pq = [(0, K - 1)]
        while pq:
            _, node = heapq.heappop(pq)
            for next_node, weight in graph[node]:
                tmp = dist[node] + weight
                if tmp < dist[next_node]:
                    dist[next_node] = tmp
                    heapq.heappush(pq, (tmp, next_node))
        if max(dist) == float("inf"):
            return -1
        else:
            return max(dist)
