# https://leetcode.com/problems/h-index

class Solution:
    def hIndex(self, citations):
        l, r = 0, len(citations)
        N = len(citations)
        ans = []
        while l <= r:
            h = (l + r) // 2
            at_least = sum([h <= cite for cite in citations])
            print(h, at_least)
            # no_more_than = sum([cite <= h for cite in citations])
            # less_than = sum([cite < h for cite in citations])
            if at_least == h:
                ans.append(h)
                l = h + 1
            elif at_least < h:
                r = h - 1
            else:
                ans.append(h)
                l = h + 1
        return max(ans)
            
        