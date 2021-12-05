# https://leetcode.com/problems/construct-target-array-with-multiple-sums

import heapq
from typing import List

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1
        max_heap = [-num for num in target]
        heapq.heapify(max_heap)
        max_val = -1 * heapq.heappop(max_heap)
        cur_sum = sum(target)
        
        while 1 < max_val:
            cur_sum -= max_val
            if (max_val <= cur_sum) or (cur_sum == 0):
                return False 
            val = max_val % cur_sum
            cur_sum += val
            heapq.heappush(max_heap, -val)
            max_val = -1 * heapq.heappop(max_heap)
        return True
  