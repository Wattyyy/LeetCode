# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts

from typing import List


class Solution:
    def maxArea(
        self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]
    ) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        verticalCuts.append(w)

        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)

        h_val = 0
        for i in range(len(horizontalCuts)):
            if i + 1 == len(horizontalCuts):
                continue
            h_val = max(h_val, horizontalCuts[i + 1] - horizontalCuts[i])

        v_val = 0
        for i in range(len(verticalCuts)):
            if i + 1 == len(verticalCuts):
                continue
            v_val = max(v_val, verticalCuts[i + 1] - verticalCuts[i])

        M = 7 + 10 ** 9
        return (h_val % M) * (v_val % M) % M
