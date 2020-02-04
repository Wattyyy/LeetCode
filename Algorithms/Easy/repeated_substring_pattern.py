# https://leetcode.com/problems/repeated-substring-pattern/

class Solution:
    def repeatedSubstringPattern(self, s):
        N = len(s)
        if N==1:
            return False

        # divide into i parts
        for i in range(2, N+1):
            if N % i != 0:
                continue
            div = N // i
            tmp_set = set()
            for j in range(0, N, div):
                tmp_set.add(s[j:j+div])
            if len(tmp_set)==1:
                return True
        return False

