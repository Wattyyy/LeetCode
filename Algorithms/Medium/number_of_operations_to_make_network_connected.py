# https://leetcode.com/problems/number-of-operations-to-make-network-connected/

class UnionFind:
    def __init__(self, N):
        self.node2par = {i:i for i in range(N)}
        self.rank = {i:0 for i in range(N)}
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
    def makeConnected(self, n, connections):
        uf = UnionFind(n)
        redundant_edge = 0
        for u, v in connections:
            if uf.find_par(u) == uf.find_par(v):
                redundant_edge += 1
            else:
                uf.unite(u, v)
        isolated = uf.count - 1
        if redundant_edge < isolated:
            return -1
        else:
            return isolated

        
