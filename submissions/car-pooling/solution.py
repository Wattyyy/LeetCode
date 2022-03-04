from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passengers = [array[0] for array in trips]
        starts = [array[1] for array in trips]
        ends = [array[2] for array in trips]

        p_trends = [0] * (max(ends) + 1)
        for (p, s, e) in zip(passengers, starts, ends):
            p_trends[s] += p
            p_trends[e] -= p

        for i, _ in enumerate(p_trends):
            if i == 0:
                continue
            else:
                p_trends[i] += p_trends[i - 1]

        return all([p <= capacity for p in p_trends])
