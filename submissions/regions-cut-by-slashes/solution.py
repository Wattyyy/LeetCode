# https://leetcode.com/problems/regions-cut-by-slashes


class UnionFind:
    def __init__(self, N):
        self.node2par = {i: i for i in range(N)}
        self.rank = {i: 0 for i in range(N)}
        self.count = N

    def find_par(self, x):
        if self.node2par[x] == x:
            return x
        else:
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
    def regionsBySlashes(self, grid):
        if not grid:
            return 0
        N = len(grid)
        uf = UnionFind(4 * (N ** 2))
        for h in range(N):
            for w in range(N):
                # set starting point
                sp = (4 * N) * h + 4 * w
                if grid[h][w] == "/":
                    uf.unite(sp, sp + 3)
                    uf.unite(sp + 1, sp + 2)

                elif grid[h][w] == "\\":
                    uf.unite(sp, sp + 1)
                    uf.unite(sp + 2, sp + 3)

                else:
                    uf.unite(sp, sp + 1)
                    uf.unite(sp, sp + 2)
                    uf.unite(sp, sp + 3)

                if h != 0:
                    # unite upper grid
                    uf.unite(sp, (sp - 4 * N) + 2)
                if w != N - 1:
                    # unite right grid
                    uf.unite(sp + 1, (sp + 4) + 3)
                if h != N - 1:
                    # unite lower grid
                    uf.unite(sp + 2, (sp + 4 * N))
                if w != 0:
                    # unite left grid
                    uf.unite(sp + 3, (sp - 4) + 1)

        return uf.count
