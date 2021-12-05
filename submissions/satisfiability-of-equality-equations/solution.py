# https://leetcode.com/problems/satisfiability-of-equality-equations

class UnionFind:
    def __init__(self):
        self.node2par = {chr(i + 97): chr(i + 97) for i in range(26)}
        
    def find_par(self, x):
        if self.node2par[x] == x:
            return x
        par = self.find_par(self.node2par[x])
        return par
    
    def unite(self, x, y):
        x, y = self.find_par(x), self.find_par(y)
        if x == y:
            return
        if x < y:
            self.node2par[y] = x
        else:
            self.node2par[x] = y
        
class Solution:
    def equationsPossible(self, equations):
        uf = UnionFind()
        neqs = []
        for eq in equations:
            if eq[1] == '=':
                uf.unite(eq[0], eq[-1])
            else:
                neqs.append(eq)
        for neq in neqs:
            if uf.find_par(neq[0]) == uf.find_par(neq[-1]):
                return False
        return True
