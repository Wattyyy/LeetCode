# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/submissions/

from collections import defaultdict

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def create_graph(self, node, prev):
        if prev:
            self.graph[node.val].append(prev.val)
        if not node.left and not node.right:
            return
        if node.left:
            self.graph[node.val].append(node.left.val)
            self.create_graph(node.left, node)
        if node.right:
            self.graph[node.val].append(node.right.val)
            self.create_graph(node.right, node)


    def distanceK(self, root, target, K):
        self.create_graph(root, None)
        res, visited = [], set()
        nx_nodes = [(target.val, 0)]
        res = []
        while nx_nodes:
            node_val, dist = nx_nodes.pop(0)
            if dist == K:
                res.append(node_val)
            visited.add(node_val)
            for next_node_val in self.graph[node_val]:
                if next_node_val not in visited:
                    nx_nodes.append((next_node_val, dist+1))
        return res


