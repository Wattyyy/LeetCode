# https://leetcode.com/problems/all-paths-from-source-lead-to-destination

from collections import defaultdict, deque
import sys

sys.setrecursionlimit(10 ** 6)


class Solution:
    def __init__(self):
        self.ans = True

    def dfs(self, v, target, graph, cnt):
        if not self.ans:
            return
        if cnt > 25000:
            self.ans = False
            return
        if v == target:
            if len(graph[v]) == 0:
                return
            self.ans = False
            return

        if not graph[v]:
            self.ans = False
            return

        for nv in graph[v]:
            self.dfs(nv, target, graph, cnt + 1)

    def leadsToDestination(self, n, edges, source, destination):
        if edges == [[]]:
            return source == destination
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        self.dfs(source, destination, graph, 0)
        return self.ans
