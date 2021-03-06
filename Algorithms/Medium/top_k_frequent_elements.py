# https://leetcode.com/problems/top-k-frequent-elements/

import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums, k):
        d = defaultdict(int)
        for num in nums:
            d[num] -= 1
        heap = []
        heapq.heapify(heap)
        for key, val in d.items():
            heapq.heappush(heap, (val, key))
        ans = []
        for i in range(k):
            _, idx = heapq.heappop(heap)
            ans.append(idx)
        return ans
