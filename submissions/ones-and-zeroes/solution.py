# https://leetcode.com/problems/ones-and-zeroes

from collections import defaultdict


class Solution:
    def findMaxForm(self, strs, m, n):
        N = len(strs)
        dp = [
            [[0 for _ in range(n + 1)] for __ in range(m + 1)] for ___ in range(N + 1)
        ]
        cnt_dic = defaultdict(tuple)
        for i, string in enumerate(strs):
            cnt_dic[i + 1] = (string.count("0"), string.count("1"))
        for i in range(1, N + 1):
            for j in range(m + 1):
                for k in range(n + 1):
                    zero_cnt, one_cnt = cnt_dic[i]
                    if 0 <= j - zero_cnt and 0 <= k - one_cnt:
                        dp[i][j][k] = max(
                            dp[i - 1][j][k], dp[i - 1][j - zero_cnt][k - one_cnt] + 1
                        )
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]

        return dp[-1][-1][-1]
