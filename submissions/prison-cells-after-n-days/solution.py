# https://leetcode.com/problems/prison-cells-after-n-days

from collections import defaultdict
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        state2day, day2state = defaultdict(int), defaultdict(tuple)
        state2day[tuple(cells)] = 0
        day2state[0] = tuple(cells)
        cur = cells[:]
        d = 1
        while True:
            nx = cur[:]
            for i, v in enumerate(cur):
                if i == 0 or i == 7:
                    nx[i] = 0
                elif (cur[i-1] == cur[i+1] == 0) or (cur[i-1] == cur[i+1] == 1):
                    nx[i] = 1
                else:
                    nx[i] = 0
            key = tuple(nx)
            if key in state2day:
                if N - d < 0:
                    return list(day2state[N])
                elif N == d:
                    return nx
                else:
                    min_idx = state2day[key]
                    days_left = N - d
                    add = days_left % (d - min_idx)
                    return list(day2state[min_idx + add])

            else:
                state2day[key] = d
                day2state[d] = key
                cur = nx
                d += 1
            
            

