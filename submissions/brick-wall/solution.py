# https://leetcode.com/problems/brick-wall

from collections import Counter
from itertools import accumulate


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        cnt = Counter()
        for row in wall:
            cum_arr = list(accumulate(row))
            for i, cum_sum in enumerate(cum_arr):
                if i == len(cum_arr) - 1:
                    break
                cnt[cum_sum] += 1

        if len(cnt) == 0:
            return len(wall)
        return len(wall) - max(cnt.values())
