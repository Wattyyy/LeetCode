# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

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
            tmp = []
            nx_queue = deque([])
            N = len(queue)
            if direction == 1:
                for _ in range(N):
                    node = queue.popleft()
                    tmp.append(node.val)
                    if node.left:
                        nx_queue.append(node.left)
                    if node.right:
                        nx_queue.append(node.right)
            else:
                for _ in range(N):
                    node = queue.pop()
                    tmp.append(node.val)
                    if node.right:
                        nx_queue.appendleft(node.right)
                    if node.left:
                        nx_queue.appendleft(node.left)

            direction *= -1
            ans.append(tmp)
            queue = nx_queue
            
        return ans
