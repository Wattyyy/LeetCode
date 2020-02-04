# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s, t):
        N = len(s)
        charmap = {}
        for i in range(N):
            if s[i] not in charmap.keys():
                if t[i] not in charmap.values():
                    charmap[s[i]] = t[i]
                else:
                    return False
            elif charmap[s[i]] != t[i]:
                return False
        return True
        
