// https://leetcode.com/problems/remove-palindromic-subsequences

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == '':
            return 0
        if len(set(s)) == 1:
            return 1
        flag = True
        N = len(s)
        for i in range(N):
            if s[i] != s[N-1-i]:
                flag = False
        
        if flag:
            return 1
        else:
            return 2
        
        

