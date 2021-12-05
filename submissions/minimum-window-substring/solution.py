# https://leetcode.com/problems/minimum-window-substring

from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s, t):
        # detect corner cases
        s_cnt, t_cnt = Counter(s), Counter(t)
        if any( [s_cnt[key] < t_cnt[key] for key in t_cnt.keys()] ):
            return ''
        s_cnt = defaultdict(int)
        lp, rp = -1, 0
        ans = (-1, -1, float('inf'))
        while lp <= rp and lp < len(s) and rp < len(s):
            s_cnt[s[rp]] += 1
            if all([ val <= s_cnt[key] for key, val in t_cnt.items() ]):
                while True:
                    if rp - lp < ans[-1]:
                        ans = (lp, rp, rp - lp) 
                    nx_char = s[lp + 1]
                    if (nx_char not in t_cnt) or (nx_char in t_cnt and t_cnt[nx_char] <= s_cnt[nx_char] - 1 ):
                        lp += 1
                        s_cnt[s[lp]] -= 1
                    else:
                        break
                if rp - lp < ans[-1]:
                    ans = (lp, rp, rp - lp) 

            rp += 1
        l, r, length = ans[0], ans[1], ans[2]
        return s[r - length + 1: r + 1]        




            


        