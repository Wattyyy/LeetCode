# https://leetcode.com/problems/find-k-closest-elements

import heapq


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        min_heap = []
        for i, v in enumerate(arr):
            heapq.heappush(min_heap, (abs(x - v), v))
        res = []
        for _ in range(k):
            diff, v = heapq.heappop(min_heap)
            res.append(v)
        return sorted(res)
