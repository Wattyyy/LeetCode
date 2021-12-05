# https://leetcode.com/problems/majority-element

from collections import Counter
class Solution:
    def majorityElement(self, nums):
        cnt = Counter(nums)
        for key, value in cnt.items():
            if value > (len(nums) // 2):
                return key
        