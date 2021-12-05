# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph

from collections import defaultdict


class Solution:
    def __init__(self):
        self.visited = set()
        self.graph = defaultdict(list)

    def dfs(self, u):
        self.visited.add(u)
        for v in self.graph[u]:
            if v not in self.visited:
                self.dfs(v)

    def countComponents(self, n, edges):
        if n == 0 or edges == [[]]:
            return 0
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)
        ans = 0
        for u in range(n):
            if u not in self.visited:
                self.dfs(u)
                ans += 1
        return ans
