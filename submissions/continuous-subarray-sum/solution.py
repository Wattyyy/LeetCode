# https://leetcode.com/problems/continuous-subarray-sum

from itertools import accumulate
from collections import defaultdict


class Solution:
    def checkSubarraySum(self, nums, k):
        if len(nums) <= 1:
            return False

        if k == 0:
            cum_sum = list(accumulate(nums))
            cum_sum = [0] + cum_sum
            sum2idx = defaultdict(list)
            for i, v in enumerate(cum_sum):
                sum2idx[v].append(i)
                if 1 < len(sum2idx[v]) and 1 < (sum2idx[v][-1] - sum2idx[v][0]):
                    return True
            return False

        k = abs(k)
        cum_mod = list(accumulate(nums))
        cum_mod = [num % k for num in cum_mod]
        cum_mod = [0] + cum_mod
        mod2idx = defaultdict(list)
        for i, v in enumerate(cum_mod):
            mod2idx[v].append(i)
            if (1 < len(mod2idx[v])) and (mod2idx[v][-1] - mod2idx[v][0] > 1):
                return True
        return False
