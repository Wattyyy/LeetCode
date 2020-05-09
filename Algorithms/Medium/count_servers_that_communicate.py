# https://leetcode.com/problems/count-servers-that-communicate/

class UnionFind:
    def __init__(self, node_list):
        # type(node) == tuple
        self.node2par = {node: node for node in node_list}
        self.rank = {node: 0 for node in node_list}
        self.count = len(node_list)
    
    def find_par(self, node):
        if node == self.node2par[node]:
            return node
        else:
            res = self.node2par[node]
            return self.find_par(res)
    
    def unite(self, x, y):
        x, y = self.find_par(x), self.find_par(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.node2par[y] = x
        elif self.rank[x] < self.rank[y]:
            self.node2par[x] = y
        else:
            self.node2par[y] = x
            self.rank[x] += 1
        self.count -= 1
    
        
class Solution:
    def countServers(self, grid):
        R, C = len(grid), len(grid[0])
        node_list = []
        for r in range(R):
            for c in range(C):
                if grid[r][c] != 1:
                    continue
                node_list.append((r, c))
        
        uf = UnionFind(node_list)
        for r in range(R):
            for c in range(C):
                if grid[r][c] != 1:
                    continue
                for y in range(R):
                    if grid[y][c] == 1:
                        uf.unite((r, c), (y, c))
                for x in range(C):
                    if grid[r][x] == 1:
                        uf.unite((r, c), (r, x))
        
        for node in uf.rank.keys():
            par_node = uf.find_par(node)
            rank = uf.rank[par_node]
            uf.rank[node] = rank
            
        ans = 0
        for val in uf.rank.values():
            if val != 0:
                ans += 1
        return ans
        
        
