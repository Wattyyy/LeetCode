# https://leetcode.com/problems/find-k-th-smallest-pair-distance/

import bisect
class Solution:
    def smallestDistancePair(self, nums, k):
        nums = sorted(nums)
        n = len(nums)
        l = 0
        r = nums[n - 1] - nums[0]

        while l < r:
            cnt = 0
            m = l + (r - l) // 2

            for i in range(n):
                j = bisect.bisect_right(nums, nums[i] + m)
                cnt += j - i - 1
            
            if (cnt < k):
                l = m + 1
            else:
                r = m

        return l
