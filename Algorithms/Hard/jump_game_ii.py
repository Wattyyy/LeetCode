# https://leetcode.com/problems/jump-game-ii/

class Solution(object):
    def jump(self, nums):
        N = len(nums)
        end = min(0+nums[0], N-1)
        new_end = min(0+nums[0], N-1)
        ans = 0
        for i in range(1, N):
            val = min(N-1, i+nums[i])
            new_end = max(new_end, val)
            if i == end:
                ans += 1
                end = new_end
        return ans
