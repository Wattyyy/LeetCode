# https://leetcode.com/problems/random-point-in-non-overlapping-rectangles

import random
from bisect import bisect_left


class Solution:
    def __init__(self, rects):
        self.rects = rects
        self.weights = []
        for i, rect in enumerate(rects):
            x1, y1, x2, y2 = rect
            if i == 0:
                self.weights.append((x2 - x1 + 1) * (y2 - y1 + 1))
            else:
                val = self.weights[-1] + (x2 - x1 + 1) * (y2 - y1 + 1)
                self.weights.append(val)

    def pick(self):
        rv = random.randint(1, self.weights[-1])
        idx = bisect_left(self.weights, rv)
        x1, y1, x2, y2 = self.rects[idx]
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)
        return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
