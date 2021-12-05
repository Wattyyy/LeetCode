# https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
        self.max_dist = 0
        self.max_dist_node = None


    def create_graph(self, node):
        if not node.left and not node.right:
            return
        if node.left:
            self.graph[node].append(node.left)
            self.graph[node.left].append(node)
            self.create_graph(node.left)
        if node.right:
            self.graph[node].append(node.right)
            self.graph[node.right].append(node)
            self.create_graph(node.right)


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
            
    
    def diameterOfBinaryTree(self, root):
        if not root or (not root.left and not root.right):
            return 0
        self.create_graph(root)
        self.calc_diameter(root, set([root]), 0)
        self.max_dist = 0
        self.calc_diameter(self.max_dist_node, set([self.max_dist_node]), 0)
        return self.max_dist
        