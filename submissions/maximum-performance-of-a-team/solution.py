// https://leetcode.com/problems/maximum-performance-of-a-team

from typing import List
import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        if k == 1:
            res = 0
            for e, s in zip(efficiency, speed):
                res = max(res, e * s)
            return res

        eff_arr = []
        for e, s in zip(efficiency, speed):
            eff_arr.append((e, s))
        eff_arr = sorted(eff_arr, reverse=True)
        pq = []
        sp_sum = 0
        ans = 0
        for e, s in eff_arr:
            if len(pq) < k - 1:
                heapq.heappush(pq, s)
                sp_sum += s
                ans = max(sp_sum * e, ans)
            else:
                ans = max((sp_sum + s) * e, ans)
                if pq[0] < s:
                    rm_s = heapq.heappop(pq)
                    heapq.heappush(pq, s)
                    sp_sum = sp_sum + s - rm_s
        return ans % (7 + 10 ** 9)




                


            







        