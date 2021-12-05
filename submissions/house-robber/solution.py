# https://leetcode.com/problems/house-robber


class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = [0] + nums
        N = len(nums)
        dp = [0] * N
        dp[1] = nums[1]
        for i in range(2, N):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return max(dp)
