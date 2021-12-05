# https://leetcode.com/problems/binary-tree-level-order-traversal-ii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []
        self.ans = deque([])
        queue = [root]
        while queue:
            tmp = []
            next_queue = []
            for node in queue:
                tmp.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            self.ans.appendleft(tmp[:])
            queue = next_queue
        return self.ans

        