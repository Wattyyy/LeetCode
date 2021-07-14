// https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = deque([root])
        while queue:
            tmp = deque([])
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            for i, node in enumerate(tmp):
                if i == len(tmp) - 1:
                    break
                node.next = tmp[i + 1]
            queue = tmp
        return root

        
        