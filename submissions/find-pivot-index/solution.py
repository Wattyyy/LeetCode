// https://leetcode.com/problems/find-pivot-index

class Solution:
    def pivotIndex(self, nums):
        if not nums:
            return -1
        l_sum = 0
        r_sum = sum(nums) - nums[0]
        if l_sum == r_sum:
            return 0
        for i in range(1, len(nums)):
            r_sum -= nums[i]
            l_sum += nums[i-1]
            if r_sum == l_sum:
                return i
        return -1
        