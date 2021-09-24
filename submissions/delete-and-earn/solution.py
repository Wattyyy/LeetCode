from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_idx = max(nums)
        points = [0] * (max_idx + 1)
        for num in nums:
            points[num] += num
        dp = [0] * (max_idx + 1)
        dp[1] = points[1]
        for i in range(2, max_idx + 1):
            dp[i] = max(dp[i - 2] + points[i], dp[i - 1])

        return dp[max_idx]
