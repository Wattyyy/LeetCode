# https://leetcode.com/problems/find-the-duplicate-number

class Solution:
    def findDuplicate(self, nums):
        L = len(nums)
        for i in range(L):
            n = abs(nums[i])
            if nums[n-1] < 0:
                return n
            else:
                nums[n-1] *= -1