# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        ans = 0
        for i in range(len(nums) // 2):
            val = nums[i] + nums[-1 - i]
            ans = max(ans, val)
        return ans
