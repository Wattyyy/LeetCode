# https://leetcode.com/problems/k-closest-points-to-origin

import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        min_heap = []
        heapq.heapify(min_heap)
        for x, y in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(min_heap, [dist, x, y])
        ans = []
        for _ in range(K):
            dist, x, y = heapq.heappop(min_heap)
            ans.append([x, y])
        return ans