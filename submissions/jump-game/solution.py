# https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums):
        N = len(nums)
        dp = [False] * len(nums)
        dp[-1] = True
        nearest_true = N - 1
        for idx in reversed(range(N-1)):
            step = nums[idx]
            if nearest_true <= idx + step:
                dp[idx] = True
                nearest_true = idx
        return dp[0] == dp[-1]