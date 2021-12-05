# https://leetcode.com/problems/jump-game-vi

from typing import List
from collections import deque


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if k == 1:
            return sum(nums)
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]

        val_deque = deque([dp[0]])
        idx_deque = deque([0])
        for i, num in enumerate(nums):
            if i == 0:
                continue
            dp[i] = val_deque[0] + num
            if idx_deque[0] == i - k:
                val_deque.popleft()
                idx_deque.popleft()
            while val_deque and val_deque[-1] < dp[i]:
                val_deque.pop()
                idx_deque.pop()
            val_deque.append(dp[i])
            idx_deque.append(i)
        return dp[-1]
