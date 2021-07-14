// https://leetcode.com/problems/redundant-connection


from typing import List

class UnionFind:
    def __init__(self, N):
        self.node2par = {i:i for i in range(1, N+1)}
        self.rank = {i:0 for i in range(1, N+1)}

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
        
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)
        for u, v in edges:
            if uf.find_par(u) != uf.find_par(v):
                uf.unite(u, v)
            else:
                return [u, v]

        