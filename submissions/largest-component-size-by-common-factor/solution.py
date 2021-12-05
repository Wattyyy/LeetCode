# https://leetcode.com/problems/largest-component-size-by-common-factor

from typing import List, Union
from collections import defaultdict
from math import sqrt


class UnionFind:
    def __init__(self, nums):
        self.node2par = {num: num for num in nums}
        self.rank = {num: 0 for num in nums}
        self.count = {num: 1 for num in nums}

    def find_par(self, x):
        if self.node2par[x] != x:
            x = self.find_par(self.node2par[x])
        return x

    def unite(self, x, y):
        x, y = self.find_par(x), self.find_par(y)
        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            self.node2par[x] = y
            self.count[y] += self.count[x]
        else:
            self.node2par[y] = x
            self.count[x] += self.count[y]

        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        uf = UnionFind(A)
        divisor_to_nums = defaultdict(list)
        for num in A:
            for i in range(1, int(sqrt(num)) + 1):
                if num % i == 0:
                    divisor_to_nums[i].append(num)
                    if i != num // i:
                        divisor_to_nums[num // i].append(num)
        del divisor_to_nums[1]

        for key, ls in divisor_to_nums.items():
            if len(ls) == 1:
                continue
            for i, num in enumerate(ls):
                if i == len(ls) - 1:
                    break
                num2 = ls[i + 1]
                uf.unite(num, num2)

        res = max(uf.count.values())
        return res
