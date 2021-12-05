# https://leetcode.com/problems/find-all-duplicates-in-an-array

class Solution:
    def findDuplicates(self, nums):
        ans = []
        for i, v in enumerate(nums):
            if nums[abs(v)-1] < 0:
                ans.append(abs(v))
            else:
                nums[abs(v)-1] *= -1
        return ans
        