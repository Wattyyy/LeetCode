// https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums):
        hs = set()
        for num in nums:
            hs.add(num)
        return len(hs)!=len(nums)
        