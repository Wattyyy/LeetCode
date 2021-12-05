# https://leetcode.com/problems/binary-tree-level-order-traversal


from collections import deque
from typing import List


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            ls = []
            next_queue = deque([])
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
                ls.append(node.val)
            res.append(ls[:])
            queue = next_queue
        return res
