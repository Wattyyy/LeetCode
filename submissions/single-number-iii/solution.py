// https://leetcode.com/problems/single-number-iii

from collections import Counter
class Solution:
    def singleNumber(self, nums):
        cnt = Counter(nums)
        res = []
        for k, v in cnt.items():
            if v == 1:
                res.append(k)
        return res
        