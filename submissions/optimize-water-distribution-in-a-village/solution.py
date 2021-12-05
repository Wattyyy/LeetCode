# https://leetcode.com/problems/optimize-water-distribution-in-a-village

from collections import defaultdict
import heapq


class UnionFind:
    def __init__(self, N):
        self.node2par = {i: i for i in range(N)}
        self.rank = {i: 0 for i in range(N)}
        self.count = N

    def find_par(self, x):
        if self.node2par[x] != x:
            x = self.find_par(self.node2par[x])
        return x

    def unite(self, x, y):
        x, y = self.find_par(x), self.find_par(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.node2par[x] = y
        else:
            self.node2par[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        self.count -= 1


class Solution:
    def minCostToSupplyWater(self, n, wells, pipes):
        graph = defaultdict(list)
        uf = UnionFind(n + 1)
        min_heap = []
        heapq.heapify(min_heap)
        for i, w in enumerate(wells):
            heapq.heappush(min_heap, (w, 0, i + 1))
        for u, v, w in pipes:
            heapq.heappush(min_heap, (w, u, v))

        ans = 0
        while 1 < uf.count and min_heap:
            w, u, v = heapq.heappop(min_heap)
            if uf.find_par(u) != uf.find_par(v):
                uf.unite(u, v)
                ans += w
        return ans
