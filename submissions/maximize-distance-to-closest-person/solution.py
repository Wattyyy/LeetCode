# https://leetcode.com/problems/maximize-distance-to-closest-person

from bisect import bisect_left


class Solution:
    def maxDistToClosest(self, seats):
        num_set = set()
        sorted_arr = []
        for i, v in enumerate(seats):
            if v == 1:
                sorted_arr.append(i)
                num_set.add(i)

        res = -1
        for i, _ in enumerate(seats):
            if i in num_set:
                continue
            idx = bisect_left(sorted_arr, i)
            if idx == 0:
                res = max(res, sorted_arr[0])
            elif idx == len(sorted_arr):
                res = max(res, i - sorted_arr[-1])
            else:
                mid = (sorted_arr[idx] + sorted_arr[idx - 1]) // 2
                res = max(res, min(sorted_arr[idx] - mid, mid - sorted_arr[idx - 1]))
        print(sorted_arr)
        return res
