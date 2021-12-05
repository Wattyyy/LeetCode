# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def add(self, node, val):
        if node.val < val:
            if not node.right:
                node.right = TreeNode(val)
            else:
                self.add(node.right, val)
        else:
            if not node.left:
                node.left = TreeNode(val)
            else:
                self.add(node.left, val)

    def bstFromPreorder(self, preorder):
        root = TreeNode(preorder[0])
        for i, v in enumerate(preorder):
            if i == 0:
                continue
            self.add(root, v)
        return root
