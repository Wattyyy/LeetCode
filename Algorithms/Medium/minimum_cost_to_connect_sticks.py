# https://leetcode.com/problems/minimum-cost-to-connect-sticks/

import heapq
class Solution:
    def connectSticks(self, sticks):
        heapq.heapify(sticks)
        res, cnt = 0, 0
        while len(sticks) > 1:
            x = heapq.heappop(sticks)
            y = heapq.heappop(sticks)
            res += (x + y)
            heapq.heappush(sticks, x + y)
        return res


        
