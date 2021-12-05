# https://leetcode.com/problems/path-with-maximum-probability

from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            prob = succProb[i]
            graph[u].append((v, prob))
            graph[v].append((u, prob))
        dist = [0.0] * n
        dist[start] = 1.0
        max_heap = [(-1.0, start)]
        while max_heap:
            val, node = heapq.heappop(max_heap)
            dist[node] = max(dist[node], abs(val))
            for nv, prob in graph[node]:
                if (dist[nv] < abs(val) * prob):
                    dist[nv] = abs(val) * prob
                    heapq.heappush(max_heap, (-1 * abs(val) * prob, nv))

        return dist[end]

        
        