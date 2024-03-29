# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference

from collections import defaultdict


class Solution:
    def longestSubsequence(self, arr, difference):
        if not arr:
            return 0
        if len(arr) == 1:
            return 1
        N = len(arr)
        dp = [0 for _ in range(N)]
        dp[-1] = 1
        val2len = defaultdict(int)
        for i in reversed(range(N)):
            val = arr[i]
            val2len[val] = max(val2len[val], val2len[val + difference] + 1)
            if i != N - 1:
                dp[i] = max(dp[i + 1], val2len[val])
        return dp[0]
