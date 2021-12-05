# https://leetcode.com/problems/is-graph-bipartite

class UnionFind():
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
    def isBipartite(self, graph):
        if graph == [[]]:
            return True
        uf = UnionFind(len(graph))
        for i, nodes in enumerate(graph):
            for j in nodes:
                if uf.find_par(i) == uf.find_par(j):
                    return False
            for j in range(len(nodes)):
                for k in range(j+1, len(nodes)):
                    uf.unite(nodes[j], nodes[k])
        return 1 < uf.count