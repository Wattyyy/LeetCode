# https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums):
        l, r = 1, len(nums)
        while l < r:
            m = (l + r) // 2
            cnt = sum([num <= m for num in nums])
            if m < cnt:
                r = m
            else:
                l = m + 1
        return l
        
        
