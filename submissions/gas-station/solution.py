from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        arr = [(g - c) for g, c in zip(gas, cost)]
        if sum(arr) < 0:
            return -1

        cum_arr = []
        for i, v in enumerate(arr):
            if i == 0:
                cum_arr.append(v)
            else:
                cum_arr.append(cum_arr[-1] + v)

        min_val = min(cum_arr)
        for i, v in enumerate(cum_arr):
            if v == min_val:
                return (i + 1) % len(cum_arr)


