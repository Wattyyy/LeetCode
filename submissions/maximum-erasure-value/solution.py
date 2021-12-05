# https://leetcode.com/problems/maximum-erasure-value

from collections import Counter
from typing import List
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        num_cnt = Counter()
        num_cnt[nums[0]] += 1
        l, r = 0, 1
        ans = 0
        tmp = nums[0]
        while r < len(nums):
            r_num = nums[r]
            while 0 < num_cnt[r_num]:
                l_num = nums[l]
                num_cnt[l_num] -= 1
                tmp -= l_num
                l += 1
            num_cnt[r_num] += 1
            tmp += r_num
            ans = max(ans, tmp)
            r += 1

        return ans
        
        


