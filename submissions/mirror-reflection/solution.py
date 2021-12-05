# https://leetcode.com/problems/mirror-reflection


class Solution:
    def mirrorReflection(self, p, q):
        if q == 0:
            return 0
        i = 0
        val = 0
        while True:
            val += q
            i += 1
            if (i % 2 == 0) and (val % p == 0):
                return 2
            elif (i % 2 == 1) and (val % (2 * p) == 0):
                return 0
            elif (i % 2 == 1) and (val % p == 0):
                return 1
            else:
                continue
