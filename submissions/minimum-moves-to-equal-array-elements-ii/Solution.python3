// https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if len(nums) % 2 == 1:
            mid = nums[len(nums) // 2]
        else:
            mid = (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) // 2
        res = 0
        for num in nums:
            res += abs(num - mid)
        return res
            
            
        
        