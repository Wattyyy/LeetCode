# https://leetcode.com/problems/reduce-array-size-to-the-half

from collections import Counter


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        ls = []
        for _, v in Counter(arr).items():
            ls.append(v)
        ls = sorted(ls)
        val = 0
        cnt = 1
        while ls:
            val += ls.pop(-1)
            if len(arr) // 2 <= val:
                return cnt
            cnt += 1
