// https://leetcode.com/problems/maximize-score-after-n-operations

from itertools import combinations
from math import gcd
import sys
sys.setrecursionlimit(10 ** 6)

class Solution:
    def maxScore(self, nums):
        N = len(nums)
        dp = [-1] * (2 ** N)
        gcds = {(i, j): gcd(nums[i], nums[j]) for (i, j) in combinations(range(N), 2)}

        def rec(bitmask):
            if -1 < dp[bitmask]:
                return dp[bitmask]
            if bitmask == 0:
                return 0
            idx_list = [idx for idx in range(N) if (bitmask & (1 << idx))]
            ret = -float('INF')
            for i, j in combinations(idx_list, 2):
                if bitmask & (1 << i) and bitmask & (1 << j):
                    new_bitmask = bitmask ^ (1 << i) ^ (1 << j)
                    ret = max( ret, rec(new_bitmask) + gcds[(i, j)] * (1 + (N - len(idx_list)) // 2) )
            dp[bitmask] = ret
            return ret
        
        res = rec(2 ** N - 1)
        return res