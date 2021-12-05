# https://leetcode.com/problems/random-pick-with-weight

# https://leetcode.com/problems/random-pick-with-weight/

import random
from bisect import bisect_right
from itertools import accumulate

class Solution:
    def __init__(self, w):
        self.max = sum(w)
        self.weight = list(accumulate(w))

    def pickIndex(self):
        rand = random.randint(0, self.max - 1)
        return bisect_right(self.weight, rand)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()