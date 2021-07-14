// https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order

import heapq
class Solution:
    def minSubsequence(self, nums):
        new = []
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        while sum(new) <= abs(sum(max_heap)):
            num = heapq.heappop(max_heap)
            new.append(abs(num))
        return new
        
        
s = Solution()
nums = [4,4,7,6,7]
print(s.minSubsequence(nums))