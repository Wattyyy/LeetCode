// https://leetcode.com/problems/move-zeroes

class Solution:
    def moveZeroes(self, nums):
        zeroes = []
        for i, v in enumerate(nums):
            if v == 0:
                zeroes.append(i)
            if v != 0 and len(zeroes) != 0:
                zero_idx = zeroes.pop(0)
                nums[i], nums[zero_idx] = nums[zero_idx], nums[i]
                zeroes.append(i)
     