# https://leetcode.com/problems/contiguous-array

from itertools import accumulate
from collections import defaultdict


class Solution:
    def findMaxLength(self, nums):
        for i, v in enumerate(nums):
            if v == 0:
                nums[i] = -1
        nums = [0] + nums
        cum_sum = list(accumulate(nums))
        dp = defaultdict(list)
        for i, v in enumerate(cum_sum):
            dp[v].append(i)
        ans = 0
        for v in dp:
            if 2 <= len(dp[v]):
                ans = max(ans, dp[v][-1] - dp[v][0])
        return ans
