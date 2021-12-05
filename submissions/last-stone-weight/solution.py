# https://leetcode.com/problems/last-stone-weight

import heapq
class Solution:
    def lastStoneWeight(self, stones):
        max_heap = []
        for i, v in enumerate(stones):
            heapq.heappush(max_heap, (-v, i))
        while 1 < len(max_heap):
            x, x_idx = heapq.heappop(max_heap)
            y, y_idx= heapq.heappop(max_heap)
            x, y = abs(x), abs(y)
            if x > y:
                x = x - y
                heapq.heappush(max_heap, (-x, x_idx))
            elif x < y:
                y = y - x
                heapq.heappush(max_heap, (-y, y_idx))
        if len(max_heap) == 1:
            return abs(max_heap[0][0])
        else:
            return 0
        