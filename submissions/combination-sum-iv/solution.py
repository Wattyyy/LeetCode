# https://leetcode.com/problems/combination-sum-iv

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        dp = [0 for _ in range(target + 1)]
        for i in range(1, target + 1):
            for num in nums:
                if i > num:
                    dp[i] += dp[i - num]
                elif i == num:
                    dp[i] += 1
                else:
                    break

        return dp[target]
