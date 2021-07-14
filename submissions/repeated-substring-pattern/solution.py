// https://leetcode.com/problems/repeated-substring-pattern

from math import sqrt
class Solution:
    def repeatedSubstringPattern(self, s):
        ans = False
        N = len(s)
        if N <= 1:
            return False
        factors = set()
        for i in range(1, int(sqrt(N)) + 1):
            if N % i == 0:
                factors.add(i)
                factors.add(N // i)
        factors.remove(N)

        for i in factors:
            tmp = set()
            flag = True
            for j in range(0, N, i):
                if j == 0:
                    tmp.add(s[:i])
                elif s[j:j+i] not in tmp:
                    flag = False
                    break
            if flag:
                ans = True

        return ans


        