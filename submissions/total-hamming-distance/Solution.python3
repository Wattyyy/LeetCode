// https://leetcode.com/problems/total-hamming-distance

from collections import Counter
class Solution:
    def __init__(self):
        self.count = Counter()
        
    def bitcount(self, num):
        cnt = 0
        while num:
            if num & 1:
                self.count[cnt] += 1
            cnt += 1
            num = num >> 1

    def totalHammingDistance(self, nums):
        if not nums:
            return 0
        N = len(nums)
        for num in nums:
            self.bitcount(num)
        res = 0
        for key in self.count:
            res += (N - self.count[key]) * self.count[key]
        return res

        