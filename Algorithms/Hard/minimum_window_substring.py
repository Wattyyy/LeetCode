# https://leetcode.com/problems/minimum-window-substring/

from collections import Counter
class Solution:
    def minWindow(self, s, t):
        s_cnt, t_cnt = Counter(s), Counter(t)
        for char in t_cnt:
            if s_cnt[char] < t_cnt[char]:
                return ''

        ans = (len(s), 0, len(s)-1)
        slide_cnt = Counter()
        l, r = 0, 0
        while r < len(s):
            slide_cnt[s[r]] += 1
            if any([slide_cnt[key] < t_cnt[key] for key in t_cnt]):
                r += 1
            else:
                while all([t_cnt[key] <= slide_cnt[key] for key in t_cnt]):
                    if (r - l + 1) < ans[0]:
                        ans = (r - l + 1, l, r)
                    slide_cnt[s[l]] -= 1
                    l += 1
                r += 1
        
        l, r = ans[1], ans[2]
        return s[l: r+1]

