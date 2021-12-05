# https://leetcode.com/problems/subarray-sum-equals-k

from collections import defaultdict
from itertools import accumulate
from bisect import bisect_right


class Solution:
    def subarraySum(self, nums, k):
        cum2idx = defaultdict(list)
        cum_sum = list(accumulate(nums))
        cum_sum = [0] + cum_sum
        for idx, num in enumerate(cum_sum):
            cum2idx[num].append(idx)
        ans = 0
        for idx, num in enumerate(cum_sum):
            if num + k in cum2idx:
                res = bisect_right(cum2idx[num + k], idx)
                ans += len(cum2idx[num + k]) - res
        return ans
