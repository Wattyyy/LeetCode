// https://leetcode.com/problems/populating-next-right-pointers-in-each-node

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
    def connect(self, root):
        if not root:
            return None
        queue = deque([root])
        while queue:
            tmp = deque([])
            for i, node in enumerate(queue):
                if i == len(queue) - 1:
                    node.next = None
                else:
                    node.next = queue[i+1]
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp
        return root
            
                    
                    
                
        
        