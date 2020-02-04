# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        self.val = 0
        def helper(node, depth):
            if not node.children:
                self.val = max(depth, self.val)
                return 
            else:
                for child in node.children:
                    helper(child, depth+1)
        helper(root, 1)
        return self.val
