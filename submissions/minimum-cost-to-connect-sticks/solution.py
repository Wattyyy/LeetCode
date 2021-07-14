// https://leetcode.com/problems/minimum-cost-to-connect-sticks

import heapq
class Solution:
    def connectSticks(self, sticks):
        heapq.heapify(sticks)
        ans = 0
        while 1 < len(sticks):
            x = heapq.heappop(sticks)
            y = heapq.heappop(sticks)
            ans += x + y
            heapq.heappush(sticks, x + y)
        return ans