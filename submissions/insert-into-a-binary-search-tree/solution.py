# https://leetcode.com/problems/insert-into-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        node = TreeNode(val)
        def insert(current, node):
            if current.val < node.val:
                if current.right is None:
                    current.right = node
                else:
                    insert(current.right, node)
            else:
                if current.left is None:
                    current.left = node
                else:
                    insert(current.left, node)
        insert(root, node)
        return root
        