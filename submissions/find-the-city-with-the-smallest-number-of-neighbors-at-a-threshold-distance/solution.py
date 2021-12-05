# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance

from collections import defaultdict
import heapq


class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # (node, reachable cities)
        ans = (float("inf"), float("inf"))
        for i in range(n):
            dist = [float("inf")] * n
            dist[i] = 0
            pq = [(0, i)]
            while pq:
                _, node = heapq.heappop(pq)
                for next_node, weight in graph[node]:
                    tmp = dist[node] + weight
                    if tmp < dist[next_node]:
                        dist[next_node] = tmp
                        heapq.heappush(pq, (tmp, next_node))

            val = sum([d <= distanceThreshold for d in dist])
            if val <= ans[1]:
                ans = (i, val)

        return ans[0]
