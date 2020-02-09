# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums):
        N = len(nums)
        end = 0
        for i in range(N):
            if end < i:
                return False
            end = max(end, nums[i]+i)
        return (N-1 <= end)
        
