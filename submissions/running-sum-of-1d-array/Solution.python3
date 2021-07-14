// https://leetcode.com/problems/running-sum-of-1d-array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for i, num in enumerate(nums):
            if i == 0:
                res[i] += nums[i]
            else:
                res[i] += nums[i] + res[i-1]
        return res