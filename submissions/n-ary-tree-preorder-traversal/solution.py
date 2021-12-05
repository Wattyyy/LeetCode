# https://leetcode.com/problems/n-ary-tree-preorder-traversal

from typing import List
import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def __init__(self):
        self.ans = []
    
    def traverse(self, node: 'Node'):
        self.ans.append(node.val)
        for child in node.children:
            self.traverse(child)
        return
        

    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return self.ans
        self.traverse(root)
        return self.ans
        
        
        
        
        