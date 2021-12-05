# https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums):
        i = 0
        ans = 0
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                del nums[i]
            else:
                ans+=1
                i += 1
                