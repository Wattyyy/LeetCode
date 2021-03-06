# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from bisect import bisect_left, bisect_right

class Solution:
    def index(self, nums, target):
        i = bisect_left(nums, target)
        if i != len(nums) and nums[i] == target:
            return i
        else:
            return -1

    def searchRange(self, nums, target):
        if (not nums) or (self.index(nums, target) == -1):
            return [-1, -1]
        left_idx = self.index(nums, target)
        right_idx = bisect_right(nums, target) - 1
        return [left_idx, right_idx]
