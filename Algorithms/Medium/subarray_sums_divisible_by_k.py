# https://leetcode.com/problems/subarray-sums-divisible-by-k/submissions/

from collections import defaultdict
from bisect import bisect_right

class Solution:
    def subarraysDivByK(self, A, K):
        cum_mod_sum = [0]
        for a in A:
            num = cum_mod_sum[-1] + a
            if num < 0:
                num = -1 * (abs(num) % K)
            else:
                num = num % K
            cum_mod_sum.append(num)
        mod2idx = defaultdict(list)
        for idx, mod in enumerate(cum_mod_sum):
            mod2idx[mod].append(idx)
        ans = 0
        for idx, mod in enumerate(cum_mod_sum):
            if mod in mod2idx:
                res = bisect_right(mod2idx[mod], idx)
                ans += len(mod2idx[mod]) - res
            if 0 < mod and mod - K in mod2idx:
                res = bisect_right(mod2idx[mod - K], idx)
                ans += len(mod2idx[mod - K]) - res
            elif mod < 0 and mod + K in mod2idx:
                res = bisect_right(mod2idx[mod + K], idx)
                ans += len(mod2idx[mod + K]) - res
                
        return ans
