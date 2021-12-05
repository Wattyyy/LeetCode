# https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s):
        if not s:
            return 0
        ls = s.split(' ')
        N = len(ls)
        for i in reversed(range(N)):
            if ls[i] == '':
                del ls[i]
        if ls:
            return len(ls[-1])
        else:
            return 0
        
            
        