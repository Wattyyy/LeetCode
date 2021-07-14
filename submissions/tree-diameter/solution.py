// https://leetcode.com/problems/tree-diameter

from collections import defaultdict
class Solution:
    def __init__(self):
        self.max_dist = 0
        self.max_dist_node = -1


    def calc_diameter(self, node, visited, dist):
        flag = False
        for nx_node in self.graph[node]:
            if nx_node not in visited:
                flag = True
                break
        if flag:
            for nx_node in self.graph[node]:
                if nx_node not in visited:
                    visited.add(nx_node)
                    self.calc_diameter(nx_node, visited, dist+1)
                    visited.remove(nx_node)
        else:
            if self.max_dist <= dist:
                self.max_dist = dist
                self.max_dist_node = node
                return 


    def treeDiameter(self, edges):
        if len(edges) == 0:
            return 0
        self.graph = defaultdict(list)
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)
        root = edges[0][0]
        self.calc_diameter(node=root, visited=set([root]), dist=0)
        farthest_node = self.max_dist_node
        self.max_dist = 0
        self.calc_diameter(node=farthest_node, visited=set([farthest_node]), dist=0)
        return self.max_dist
        

        

        