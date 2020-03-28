# https://leetcode.com/problems/check-if-it-is-a-straight-line/

from collections import defaultdict
from math import gcd

class Solution:
    def checkStraightLine(self, coordinates):
        d = defaultdict(int)
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        a, b, c = (x1 - x2), (y2 - y1), (y1 * x2 - x1 * y2)
        gcd1 = gcd(abs(a), abs(b))
        gcd2 = gcd(gcd1, abs(c))
        a, b, c = a // gcd2, b // gcd2, c // gcd2
        d[(a, b, c)] += 1
        if 2 < len(coordinates):
            for i in range(3, len(coordinates)):
                x2, y2 = coordinates[i]
                a, b, c = (x1 - x2), (y2 - y1), (y1 * x2 - x1 * y2)
                gcd1 = gcd(abs(a), abs(b))
                gcd2 = gcd(gcd1, abs(c))
                a, b, c = a // gcd2, b // gcd2, c // gcd2
                if (a, b, c) in d:
                    d[(a, b, c)] += 1
                elif (-a, -b, -c) in d:
                    d[(-a, -b, -c)] += 1
                else:
                    d[(a, b, c)] += 1
    
        return len(d) == 1
