# https://leetcode.com/problems/largest-number-at-least-twice-of-others

class Solution:
    def dominantIndex(self, nums):
        if len(nums)==1:
            return 0
        first, second = (-1, -1), (-2, -2)
        for i in range(len(nums)):
            if first[0] <= nums[i]:
                second = first
                first = (nums[i], i)
            elif second[0] <= nums[i]:
                second = (nums[i], i)
            else:
                continue
        if second[0]*2 <= first[0]:
            return first[1]
        else:
            return -1
        
        