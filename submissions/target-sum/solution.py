# https://leetcode.com/problems/target-sum

# https://leetcode.com/problems/target-sum/

from collections import defaultdict


class Solution:
    def findTargetSumWays(self, nums, S):
        dp = defaultdict(int)
        dp[-nums[0]] += 1
        dp[nums[0]] += 1
        for i, num in enumerate(nums):
            if i == 0:
                continue
            new = defaultdict(int)
            for key in dp.keys():
                new[key + num] += dp[key]
                new[key - num] += dp[key]
            dp = new
        return dp[S]
