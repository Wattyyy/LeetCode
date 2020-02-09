# https://leetcode.com/problems/4sum-ii/

from collections import Counter
class Solution:
    def fourSumCount(self, A, B, C, D):
        A, B, C, D = sorted(A), sorted(B), sorted(C), sorted(D)
        CD = []
        for c in C:
            for d in D:
                CD.append(-c-d)
        CD = Counter(CD)
        ans = 0
        for a in A:
            for b in B:
                if a+b in CD.keys():
                    ans += CD[a+b]
        return ans
