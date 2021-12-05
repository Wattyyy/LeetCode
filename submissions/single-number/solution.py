# https://leetcode.com/problems/single-number

class Solution:
    def singleNumber(self, nums):
        res = 0 
        for num in nums:
            res = res ^ num
        return res
        