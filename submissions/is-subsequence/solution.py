# https://leetcode.com/problems/is-subsequence


class Solution:
    def isSubsequence(self, s, t):
        i = 0
        for j in range(len(t)):
            if i == len(s):
                return True
            if s[i] == t[j]:
                i += 1
        return i == len(s)
