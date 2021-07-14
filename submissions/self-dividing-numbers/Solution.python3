// https://leetcode.com/problems/self-dividing-numbers

class Solution:
    def selfDividingNumbers(self, left, right):
        ans = []
        for n in range(left, right + 1):
            str_n = str(n)
            flag = True
            for d in str_n:
                if int(d) == 0:
                    flag = False
                elif n % int(d) != 0:
                    flag = False
            if flag:
                ans.append(n)
        return ans