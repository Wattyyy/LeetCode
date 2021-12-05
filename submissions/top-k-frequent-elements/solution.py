# https://leetcode.com/problems/top-k-frequent-elements

import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        cnt = Counter(nums)
        print(cnt)
        min_heap = []
        for key, val in cnt.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (val, key))
            else:
                if min_heap[0][0] < val:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (val, key))
            
        res = []
        for v, k in min_heap:
            res.append(k)
        return res
                