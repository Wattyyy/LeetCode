# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/

from collections import defaultdict
class Solution:
    def maxSubArrayLen(self, nums, k):
        if not nums:
            return 0
        N = len(nums)
        ans = 0
        val2idx = defaultdict(list)
        cum_sum = [0] * len(nums)
        cum_sum[0] += nums[0]
        for i in range(1, len(nums)):
            cum_sum[i] = cum_sum[i-1] + nums[i]
        
        for i in range(N):
            val2idx[k-cum_sum[i]].append(i)
            if k - cum_sum[i] == 0:
                ans = max(ans, i + 1)
        
        for i in range(N):
            if -cum_sum[i] in val2idx:
                # get maximum index
                idx = val2idx[-cum_sum[i]][-1]
                if idx - i >= 1:
                    ans = max(ans, idx - i)
        return ans
        

