// https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0

    def traverse(self, node, cur):
        if not node.left and not node.right:
            self.ans += int(''.join(cur), 2)
            return
        if node.left:
            cur.append(str(node.left.val))
            self.traverse(node.left, cur)
            cur.pop()
        if node.right:
            cur.append(str(node.right.val))
            self.traverse(node.right, cur)
            cur.pop()
        
    def sumRootToLeaf(self, root):
        if not root:
            return 0
        self.traverse(root, [str(root.val)])
        return self.ans
        