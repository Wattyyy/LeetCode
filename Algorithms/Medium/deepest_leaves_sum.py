# https://leetcode.com/problems/deepest-leaves-sum/solution/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
class Solution:
    def __init__(self):
        self.depth2val = defaultdict(list)

    def traverse(self, node, depth):
        self.depth2val[depth].append(node.val)
        if not node.left and not node.right:
            return
        if node.left:
            self.traverse(node.left, depth+1)
        if node.right:
            self.traverse(node.right, depth+1)
        
    def deepestLeavesSum(self, root):
        self.traverse(root, 0)
        max_depth = max(self.depth2val.keys())
        return sum(self.depth2val[max_depth])
        
        
