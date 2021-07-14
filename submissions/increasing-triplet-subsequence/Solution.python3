// https://leetcode.com/problems/increasing-triplet-subsequence

from bisect import bisect_left
class Solution:
    def increasingTriplet(self, nums):
        arr = [float('inf')] * 3
        for _, num in enumerate(nums):
            idx = bisect_left(arr, num)
            if idx < 3:
                arr[idx] = num
        return (float('inf') not in arr)
            
        