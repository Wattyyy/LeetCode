// https://leetcode.com/problems/n-ary-tree-level-order-traversal

# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        ans = []
        queue = deque([root])
        while queue:
            node_list = []
            val_list = []
            for node in queue:
                val_list.append(node.val)
                if node.children:
                    for child in node.children:
                        node_list.append(child)
            ans.append(val_list)
            queue = deque(node_list)
        return ans
