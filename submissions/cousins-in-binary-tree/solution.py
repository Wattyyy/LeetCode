// https://leetcode.com/problems/cousins-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
class Solution:
    def search(self, cur, target, parent, depth):
        if cur.val == target:
            self.d[cur.val] = [parent.val, depth]
            return
        else:
            if cur.left is not None:
                self.search(cur.left, target, cur, depth+1)
            if cur.right is not None:
                self.search(cur.right, target, cur, depth+1)
            
            
    def isCousins(self, root, x, y):
        # x -> [parent, depth]
        # y -> [parent, depth]
        self.d = defaultdict(list)
        self.search(root, x, root, 0)
        self.search(root, y, root, 0)
        return (self.d[x][0] != self.d[y][0]) and (self.d[x][1] == self.d[y][1])
        
        
        
        
        