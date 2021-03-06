# https://leetcode.com/problems/contiguous-array/

from collections import defaultdict
class Solution:
    def findMaxLength(self, nums):
        if not nums:
            return 0
        nums = [-1 if num==0 else 1 for num in nums]
        cum_sum = [0] * len(nums)
        cum_sum[0] += nums[0]
        sum2idx = defaultdict(int)
        sum2idx[0], sum2idx[cum_sum[0]] = -1, 0
        ans = 0
        for i in range(1, len(nums)):
            cum_sum[i] = cum_sum[i-1] + nums[i]
            if cum_sum[i] not in sum2idx.keys():
                sum2idx[cum_sum[i]] = i
            else:
                ans = max(ans, i - sum2idx[cum_sum[i]])
        return ans
