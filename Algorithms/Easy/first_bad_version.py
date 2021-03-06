# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        def search(l, r):
            if l==r:
                return l
            mid = r + (l - r)//2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
            return search(l, r)
        idx = search(1, n)
        return idx
            
            
