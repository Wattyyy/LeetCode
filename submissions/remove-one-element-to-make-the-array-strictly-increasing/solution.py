# https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        N = len(nums)
        cnt = 0
        for i in range(N):
            ls = nums[:]
            ls.pop(i)
            flag = True
            for j, _ in enumerate(ls):
                if j == 0:
                    continue
                if ls[j-1] >= ls[j]:
                    flag = False
                    break
            if flag:
                return True
            
        return False