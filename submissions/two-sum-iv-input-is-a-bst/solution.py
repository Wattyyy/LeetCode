from typing import Optional


class Solution:
    def search(self, node: Optional[TreeNode], target: int):
        if target - node.val in self.set and target - node.val != node.val:
            self.flag = True
            return
        self.set.add(node.val)
        if node.left:
            self.search(node.left, target)
        if node.right:
            self.search(node.right, target)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.set = set()
        self.flag = False
        self.search(root, k)
        return self.flag
