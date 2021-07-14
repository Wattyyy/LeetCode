// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one

class Solution:
    def numSteps(self, s):
        N = len(s)
        num = 0
        for i in range(N):
            num += int(s[i]) * 2 ** (N - i - 1)
        res = 0
        while num != 1:
            if num % 2 == 1:
                num += 1
            else:
                num = num // 2
            res += 1
        return res

        
        
        