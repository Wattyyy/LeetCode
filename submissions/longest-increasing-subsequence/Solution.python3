// https://leetcode.com/problems/longest-increasing-subsequence

from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [float('inf') for _ in range(len(nums))]
        ans = 1
        for num in nums:
            idx = bisect_left(dp, num)
            ans = max(ans, idx + 1)
            dp[idx] = num
        return ans
            