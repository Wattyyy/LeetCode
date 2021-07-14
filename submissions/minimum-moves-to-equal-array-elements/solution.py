// https://leetcode.com/problems/minimum-moves-to-equal-array-elements

class Solution:
    def minMoves(self, nums):
        min_num = min(nums)
        ans = 0
        for num in nums:
            ans += num - min_num
        return ans
        