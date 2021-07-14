// https://leetcode.com/problems/combination-sum-iii

from typing import List
from itertools import combinations
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combs = list(combinations([i for i in range(1, 10)], k))
        res = []
        for tp in combs:
            if sum(tp) == n:
                res.append(list(tp))
        return res