# https://leetcode.com/problems/binary-search-tree-iterator

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BSTIterator:
    def __init__(self, root):
        self.bst_list = []
        self.root = root
        self.helper(self.root)
        self.pointer = 0

    def helper(self, root):
        if root:
            self.helper(root.left)
            self.bst_list.append(root.val)
            self.helper(root.right)

    def next(self):
        res = self.bst_list[self.pointer]
        self.pointer += 1
        return res

    def hasNext(self):
        if self.pointer < len(self.bst_list):
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
