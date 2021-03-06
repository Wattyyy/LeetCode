# https://leetcode.com/problems/count-of-smaller-numbers-after-self/

class BSTNode:
    def __init__(self, val):
        self.val = val
        self.duplicate = 1
        self.left_nodes = 0
        self.left = None
        self.right = None

class Solution:
    def countSmaller(self, nums):
        if not nums:
            return []
        if len(nums) == 1:
            return [0]
        
        N = len(nums)
        ans = [0] * N
        root = BSTNode(nums[-1])
        for i in reversed(range(N-1)):
            count = 0
            cur = root
            while True:
                if cur.val < nums[i]:
                    count += cur.left_nodes + cur.duplicate
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = BSTNode(nums[i])
                        break

                elif cur.val == nums[i]:
                    cur.duplicate += 1
                    count += cur.left_nodes
                    break

                else:
                    cur.left_nodes += 1
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = BSTNode(nums[i])
                        break
            
            ans[i] = count        
        return ans
            
        
