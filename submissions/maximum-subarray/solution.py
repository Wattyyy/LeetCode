# https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums):
        local_max = 0
        global_max = -float('inf')
        for i, v in enumerate(nums):
            local_max = max(v, local_max + v)
            global_max = max(local_max, global_max)
        return global_max