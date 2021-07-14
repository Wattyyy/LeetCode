// https://leetcode.com/problems/binary-search

from bisect import bisect_left
    
class Solution:
    def index(self, a, x):
        i = bisect_left(a, x)
        if i != len(a) and a[i] == x:
            return i
        else:
            return -1

    def search(self, nums, target):
        return self.index(nums, target)
        