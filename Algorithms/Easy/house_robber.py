# https://leetcode.com/problems/house-robber

class Solution:    
    def rob(self, nums):
        N = len(nums)
        if N==0:
            return 0
        if N==1:
            return nums[0]
        if N==2:
            return max(nums[0], nums[1])
        
        # dp[i] contains maximum value given nums[0:i]   
        dp = [0 for _ in range(N)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, N):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[N-1]
