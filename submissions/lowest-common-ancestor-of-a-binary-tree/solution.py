# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.p_list = None
        self.q_list = None
        
    def search(self, node: TreeNode, target: TreeNode , ls: List, flag: bool) -> List:
        ls.append(node)
        if node.val == target.val:
            if flag:
                self.p_list = ls[:]
            else:
                self.q_list = ls[:]
        else:
            if node.left:
                self.search(node.left, target, ls, flag)
                ls.pop()
            if node.right:
                self.search(node.right, target, ls, flag)
                ls.pop()

            
        
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.search(root, p, [], True)
        self.search(root, q, [], False)
        ans = self.p_list[0]
        for i in range( min(len(self.p_list), len(self.q_list)) ):
            if self.p_list[i].val == self.q_list[i].val:
                ans = self.p_list[i]
            else:
                break
        return ans        
        