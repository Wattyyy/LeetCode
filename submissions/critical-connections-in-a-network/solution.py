# https://leetcode.com/problems/critical-connections-in-a-network

from collections import defaultdict
from typing import List


class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        edge_set = {tuple(edge) for edge in connections}
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        tin = [float("inf")] * n
        low = [float("inf")] * n
        visited = [False] * n
        self.time = 0
        res = []

        def dfs(node, par):
            tin[node] = self.time
            low[node] = self.time
            visited[node] = True
            self.time += 1
            for child in graph[node]:
                if child == par:
                    continue
                if visited[child]:
                    low[node] = min(low[node], low[child])
                else:
                    dfs(child, node)
                    low[node] = min(low[node], low[child])
                    if low[child] > tin[node]:
                        if (child, node) in edge_set:
                            res.append([child, node])
                        else:
                            res.append([node, child])

        for v in range(n):
            if not visited[v]:
                dfs(v, -1)
        return res
