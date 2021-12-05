# https://leetcode.com/problems/search-in-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return
        if root.val == val:
            return root
        if root.val < val:
            if not root.right:
                return
            else:
                return self.searchBST(root.right, val)
        else:
            if not root.left:
                return
            else:
                return self.searchBST(root.left, val)
