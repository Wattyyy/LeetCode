# https://leetcode.com/problems/find-smallest-letter-greater-than-target

class Solution:
    def nextGreatestLetter(self, letters, target):
        N = len(letters)
        l, r = 0, N
        while l < r:
            mid = (l + r) // 2
            if letters[mid] <= target:
                l = mid + 1
            else:
                r = mid
        if l==N:
            return letters[0]
        else:
            return letters[l]
        
        
        
        