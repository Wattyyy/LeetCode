# https://leetcode.com/problems/contains-duplicate-ii

from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        d = defaultdict(int)
        for num in nums[:k+1]:
            d[num] += 1
            if 2 <= d[num]:
                return True
        for i in range(k+1, len(nums)):
            d[nums[i-k-1]] -= 1
            d[nums[i]] += 1
            if 2 <= d[nums[i]]:
                return True
                
        return False