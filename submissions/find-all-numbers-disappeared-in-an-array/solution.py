# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array


class Solution:
    def findDisappearedNumbers(self, nums):
        for num in nums:
            if nums[abs(num) - 1] < 0:
                continue
            else:
                nums[abs(num) - 1] *= -1
        res = []
        for idx, num in enumerate(nums):
            if num > 0:
                res.append(idx + 1)
        return res
