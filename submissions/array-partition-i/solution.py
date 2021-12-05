# https://leetcode.com/problems/array-partition-i


class Solution:
    def arrayPairSum(self, nums: List[int]):
        nums = sorted(nums)
        ans = 0
        for i in range(0, len(nums), 2):
            ans += nums[i]
        return ans
