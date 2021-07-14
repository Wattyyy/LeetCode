// https://leetcode.com/problems/binary-tree-paths

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []

    def backtrack(self, node, cur):
        if not node.left and not node.right:
            item = '->'.join(cur)
            self.ans.append(item)
        if node.left:
            cur.append(str(node.left.val))
            self.backtrack(node.left, cur)
            cur.pop(-1)
        if node.right:
            cur.append(str(node.right.val))
            self.backtrack(node.right, cur)
            cur.pop(-1)
        

    def binaryTreePaths(self, root):
        if not root:
            return []
        self.backtrack(root, [str(root.val)])
        return self.ans

        