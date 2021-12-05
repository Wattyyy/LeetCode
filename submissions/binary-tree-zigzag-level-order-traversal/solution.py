# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        ans = []
        queue = deque([root])
        direction = 1
        while queue:
            nx = deque([])
            tmp = []
            for node in queue:
                tmp.append(node.val)
                if direction == 1:
                    if node.left:
                        nx.appendleft(node.left)
                    if node.right:
                        nx.appendleft(node.right)
                else:
                    if node.right:
                        nx.appendleft(node.right)
                    if node.left:
                        nx.appendleft(node.left)
            ans.append(tmp)
            queue = nx
            direction *= -1
        return ans
