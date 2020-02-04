# https://leetcode.com/problems/random-pick-with-weight/

import random
from bisect import bisect_left

class Solution:
    def __init__(self, w):
        multi_dist = [0 for _ in range(len(w))]
        multi_dist[0] = w[0]
        for i in range(1, len(w)):
            multi_dist[i] = multi_dist[i-1] + w[i]
        self.multi_dist = multi_dist
    
    def pickIndex(self):
        r_int = random.randint(1, self.multi_dist[-1])
        idx = bisect_left(self.multi_dist, r_int)
        return idx
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
