# https://leetcode.com/problems/reducing-dishes

class Solution:
    def maxSatisfaction(self, satisfaction):
        N = len(satisfaction)
        satisfaction = sorted(satisfaction)
        res = 0
        for i, v in enumerate(satisfaction):
            res += v * (i + 1)
        
        start = 1
        while satisfaction:
            tmp = 0
            coef = 1
            for i in range(start, N):
                tmp += coef * satisfaction[i]
                coef += 1
            if res < tmp:
                res = tmp
                start += 1
            else:
                break
        return res

