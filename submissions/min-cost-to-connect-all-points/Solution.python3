// https://leetcode.com/problems/min-cost-to-connect-all-points

import heapq

class UnionFind:
    def __init__(self, N):
        self.node2parent = {i: i for i in range(N)}
        self.rank = {i: 0 for i in range(N)}
        self.count = N
    
    def find_parent(self, x):
        parent = self.node2parent[x]
        if parent != x:
            return self.find_parent(parent)
        else:
            return parent
    
    def unite(self, x, y):
        x, y = self.find_parent(x), self.find_parent(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.node2parent[x] = y
        else:
            self.node2parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        self.count -= 1


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        N = len(points)
        uf = UnionFind(N)

        min_heap = []
        for i in range(N):
            for j in range(i + 1, N):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(min_heap, (dist, i, j))

        ret = 0
        while min_heap:
            val, node1, node2 = heapq.heappop(min_heap)
            if uf.find_parent(node1) != uf.find_parent(node2):
                uf.unite(node1, node2)
                ret += val

        return ret            
            