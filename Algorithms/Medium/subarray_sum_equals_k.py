# https://leetcode.com/problems/subarray-sum-equals-k/

from collections import defaultdict
class Solution:
    def subarraySum(self, nums, k):
        dic = defaultdict(int)
        dic[0] = 1
        ans = 0
        cum_sum = 0
        for num in nums:
            cum_sum += num
            if cum_sum - k in dic:
                ans += dic[cum_sum - k]
            dic[cum_sum] += 1
            
        return ans
            
            
        
