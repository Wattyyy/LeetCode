// https://leetcode.com/problems/range-addition

class Solution:
    def getModifiedArray(self, length, updates):
        res = [0] * length
        for s, e, i in updates:
            res[s] += i
            if e + 1 < length:
                res[e+1] -= i
        for i in range(1, length):
            res[i] += res[i-1]
        return res 