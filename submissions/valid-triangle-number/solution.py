# https://leetcode.com/problems/valid-triangle-number

from bisect import bisect_right
class Solution:
    def triangleNumber(self, nums):
        if len(nums) < 3:
            return 0
        nums = sorted(nums)
        N = len(nums)
        ans = 0
        for i in reversed(range(0, N)):
            for j in reversed(range(0, i)):
                llim = nums[i] - nums[j]
                res = bisect_right(nums, llim)
                ans += max(0, j - res)
        return ans
