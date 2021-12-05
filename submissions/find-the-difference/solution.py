# https://leetcode.com/problems/find-the-difference

from collections import Counter
class Solution:
    def findTheDifference(self, s, t):
        s_cnt, t_cnt = Counter(s), Counter(t)
        for key in t_cnt:
            if s_cnt[key] != t_cnt[key]:
                return key
            
        
        