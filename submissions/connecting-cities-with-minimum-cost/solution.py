// https://leetcode.com/problems/connecting-cities-with-minimum-cost

import heapq

class UnionFind():
    def __init__(self, N):
        self.node2par = {i:i for i in range(1, N+1)}
        self.rank = {i:0 for i in range(1, N+1)}
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
            self.rank[x]+=1
        self.count -= 1


class Solution:
    def minimumCost(self, N, connections):
        uf = UnionFind(N)
        total_cost = 0
        min_heap = []
        heapq.heapify(min_heap)
        for u, v, w in connections:
            heapq.heappush(min_heap, (w, u, v))
        
        while min_heap:
            w, u, v = heapq.heappop(min_heap)
            if uf.find_par(u) != uf.find_par(v):
                total_cost += w
                uf.unite(u, v)
        
        if uf.count == 1:
            return total_cost
        else:
            return -1
        
        