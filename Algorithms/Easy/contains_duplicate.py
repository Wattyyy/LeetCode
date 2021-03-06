# https://leetcode.com/problems/contains-duplicate/submissions/

class Solution:
    def containsDuplicate(self, nums):
        if not nums:
            return False
        s = set()
        for num in nums:
            if num in s:
                return True
            else:
                s.add(num)
        return False
        
