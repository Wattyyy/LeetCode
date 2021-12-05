# https://leetcode.com/problems/longest-consecutive-sequence

from typing import List


class UnionFind:
    def __init__(self, nums):
        self.parent = {num: num for num in nums}
        self.rank = {num: 0 for num in nums}
        self.size = {num: 1 for num in nums}

    def find(self, node):
        if node == self.parent[node]:
            return node
        res = self.find(self.parent[node])
        return res

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
            self.size[y] += self.size[x]
        else:
            self.parent[y] = x
            self.size[x] += self.size[y]

        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        new_nums = list(set(nums))
        uf = UnionFind(new_nums)
        for num in new_nums:
            if num - 1 in uf.parent.keys():
                uf.union(num, num - 1)
            if num + 1 in uf.parent.keys():
                uf.union(num, num + 1)

        return max(uf.size.values())
