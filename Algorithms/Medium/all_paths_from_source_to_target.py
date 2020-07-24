class Solution:
    def __init__(self):
        self.ans = []
        
    def traverse(self, node, tmp):
        if node == len(self.graph) - 1:
            self.ans.append(tmp[:])
        for nx in self.graph[node]:
            tmp.append(nx)
            self.traverse(nx, tmp)
            tmp.pop(-1)
    
    def allPathsSourceTarget(self, graph):
        self.graph = graph
        self.traverse(0, [0])
        return self.ans
        
