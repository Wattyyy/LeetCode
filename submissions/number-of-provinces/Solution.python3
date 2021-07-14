// https://leetcode.com/problems/number-of-provinces

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
    def findCircleNum(self, M: List[List[int]]) -> int:
        N = len(M)
        uf = UnionFind(N)
        for u in range(N):
            for v in range(N):
                if u == v or M[u][v] != 1:
                    continue
                uf.unite(u, v)
        return uf.count

                     