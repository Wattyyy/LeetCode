// https://leetcode.com/problems/flatten-binary-tree-to-linked-list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        cur = root
        while cur:
            if cur.left:
                last = cur.left
                while last.right:
                    last = last.right
                last.right = cur.right
                cur.right = cur.left
                cur.left = None                
            cur = cur.right
            