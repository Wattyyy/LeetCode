# https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ans = False

    def backtrack(self, node, index):
        if self.ans:
            return
        if index == len(self.arr) - 1:
            if not node.left and not node.right:
                self.ans = True
                return
            return
        if node.left and node.left.val == self.arr[index + 1]:     
            self.backtrack(node.left, index + 1)
        if node.right and node.right.val == self.arr[index + 1]:
            self.backtrack(node.right, index + 1)
        

    def isValidSequence(self, root, arr):
        if not root or arr[0] != root.val:
            return False
        self.arr = arr
        self.backtrack(root, 0)
        return self.ans
        


        