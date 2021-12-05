# https://leetcode.com/problems/invert-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def swap(self, node):
        node.left, node.right = node.right, node.left
        if node.left:
            self.swap(node.left)
        if node.right:
            self.swap(node.right)

    def invertTree(self, root):
        if not root:
            return
        self.swap(root)
        return root
