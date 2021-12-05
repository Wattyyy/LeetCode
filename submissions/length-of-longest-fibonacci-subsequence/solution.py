# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence

from collections import defaultdict


class Solution:
    def lenLongestFibSubseq(self, A):
        N = len(A)
        val2idx = defaultdict(int)
        for i, v in enumerate(A):
            val2idx[v] = i
        dp = [[2 for _ in range(N)] for __ in range(N)]
        for i in range(N):
            for j in range(i + 1, N):
                if (A[i] + A[j]) in val2idx:
                    idx = val2idx[A[i] + A[j]]
                    dp[j][idx] = max(dp[j][idx], dp[i][j] + 1)
        ans = 2
        for i in range(N):
            ans = max(max(dp[i]), ans)

        if ans == 2:
            return 0
        else:
            return ans
