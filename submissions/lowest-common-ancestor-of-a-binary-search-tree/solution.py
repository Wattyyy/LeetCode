from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def search(self, node: 'TreeNode', target: 'TreeNode', ls: List) -> List:
        ls.append(node)
        if node.val == target.val:
            return ls
        if target.val < node.val:
            return self.search(node.left, target, ls)
        else:
            return self.search(node.right, target, ls)
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ls1 = self.search(root, p, [])
        ls2 = self.search(root, q, [])
        N = min(len(ls1), len(ls2))
        for i in range(N):
            if ls1[i].val != ls2[i].val:
                return ls1[i-1]
            if i == N - 1:
                return ls1[i]
