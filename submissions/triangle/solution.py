# https://leetcode.com/problems/triangle

from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [triangle[0][0]]
        for row, ls in enumerate(triangle):
            if row == 0:
                continue
            new = [float('inf')] * (row + 1)
            for i, num in enumerate(ls):
                if i == 0:
                    new[i] = min(new[i], dp[i] + num)
                elif i == len(ls) - 1:
                    new[i] = min(new[i], dp[i-1] + num)
                else:
                    new[i] = min(new[i], dp[i] + num, dp[i-1] + num)
            dp = new
        return min(dp)

        