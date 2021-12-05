# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

from bisect import bisect_left, bisect_right
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        l, r = bisect_left(nums, target), bisect_right(nums, target)
        r -= 1
        if (0 <= l < len(nums)) and (0 <= r < len(nums)) and (nums[l] == nums[r] == target):
            return [l, r]
        else:
            return [-1, -1]
        

