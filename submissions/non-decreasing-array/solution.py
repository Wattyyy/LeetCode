// https://leetcode.com/problems/non-decreasing-array

from typing import List
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        tmp1, tmp2 = nums[:], nums[:]
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                tmp1[i] = nums[i+1]
                tmp2[i+1] = nums[i]
                break
        return (sorted(tmp1) == tmp1) or (sorted(tmp2) == tmp2)