# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        self.is_same = True
        def helper(node1, node2):
            if not node1 and not node2:
                return
            elif node1 and node2 and node1.val == node2.val:
                helper(node1.left, node2.left)
                helper(node1.right, node2.right)
            else:
                self.is_same = False
                return
        helper(p, q)
        return self.is_same
        
