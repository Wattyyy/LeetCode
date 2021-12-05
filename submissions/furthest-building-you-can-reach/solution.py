# https://leetcode.com/problems/furthest-building-you-can-reach

import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        if len(heights) == 1:
            return 0

        if ladders == 0:
            bricks_sum = 0
            res = 0
            prev = heights[0]
            for i, cur in enumerate(heights):
                if i == 0:
                    continue
                if prev < cur:
                    bricks_sum += cur - prev
                prev = cur
                if bricks_sum <= bricks:
                    res = i
                else:
                    break
            return res

        min_heap = []
        prev = heights[0]
        bricks_sum = 0
        res = 0
        for i, cur in enumerate(heights):
            if i == 0:
                continue
            if prev < cur:
                diff = cur - prev
                if len(min_heap) < ladders:
                    heapq.heappush(min_heap, diff)
                elif diff < min_heap[0]:
                    bricks_sum += diff
                else:
                    heapq.heappush(min_heap, diff)
                    bricks_sum += heapq.heappop(min_heap)

            prev = cur
            if bricks_sum <= bricks:
                res = i
            else:
                break
        return res
