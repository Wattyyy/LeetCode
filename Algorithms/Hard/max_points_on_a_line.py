# https://leetcode.com/problems/max-points-on-a-line/

from collections import defaultdict, Counter
from decimal import *
class Solution:
    def maxPoints(self, points):
        N = len(points)
        if N == 1 or N == 0: 
            return N
        # (coef, intercept) -> points list
        d = defaultdict(set)
        # detect duplicate
        c = Counter([tuple(point) for point in points])
        keys = []
        for key in c:
            if c[key] <= 1: 
                keys.append(key)
        for key in keys:
            del c[key]

        for i in range(N):
            for j in range(i+1, N):
                x1, y1 = points[i]
                x2, y2 = points[j]
                # calc coef and intercept
                if x2 - x1 != 0:
                    m = Decimal(y2 - y1) / Decimal(x2 - x1)
                    b = m * (-x1) + y1
                    d[(str(m), str(b))].add((x1, y1))
                    d[(str(m), str(b))].add((x2, y2))
                else:
                    d[(str(x1))].add((x1, y1))
                    d[(str(x1))].add((x2, y2))
                    
        ans = 1
        for key, p_set in d.items():
            tmp_val = 0
            for c_key in c:
                if c_key in p_set:
                    tmp_val += (c[c_key] - 1)   
            ans = max(ans, len(d[key]) + tmp_val)
        return ans
