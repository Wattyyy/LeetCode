# https://leetcode.com/problems/find-k-pairs-with-smallest-sums

from bisect import bisect_left
import heapq
class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        min_heap = []
        for i, u in enumerate(nums1):
            for j, v in enumerate(nums2):
                min_heap.append((u + v, u, v, i, j))

        heapq.heapify(min_heap)
        ans = []
        for _ in range(k):
            if len(min_heap) == 0:
                break
            uv_sum, u, v, i, j = heapq.heappop(min_heap)
            ans.append([u, v])
        return ans